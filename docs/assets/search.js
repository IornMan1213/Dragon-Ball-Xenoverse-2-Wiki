(() => {
  const input = document.querySelector('[data-wiki-search]');
  const results = document.querySelector('[data-search-results]');
  const status = document.querySelector('[data-search-status]');
  if (!input || !results) return;

  let index = [];
  let loading = true;

  const normalize = (value) => (value || '')
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();

  const escapeHtml = (value) => String(value || '').replace(/[&<>\"]/g, (char) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '\"': '&quot;'
  }[char]));

  const excerpt = (text, query) => {
    const clean = String(text || '').replace(/\s+/g, ' ').trim();
    if (!clean) return '';
    const needle = normalize(query).split(' ')[0];
    const haystack = normalize(clean);
    const at = needle ? haystack.indexOf(needle) : -1;
    if (at < 0) return clean.slice(0, 220) + (clean.length > 220 ? '…' : '');
    const start = Math.max(0, at - 90);
    const end = Math.min(clean.length, start + 260);
    return (start ? '…' : '') + clean.slice(start, end) + (end < clean.length ? '…' : '');
  };

  const score = (item, query, tokens) => {
    const title = normalize(item.title);
    const description = normalize(item.description);
    const text = normalize(item.text);
    const path = normalize(item.path);
    let value = 0;
    if (title === query) value += 1000;
    if (title.includes(query)) value += 400;
    if (description.includes(query)) value += 180;
    if (text.includes(query)) value += 120;
    if (path.includes(query)) value += 80;
    for (const token of tokens) {
      if (title.includes(token)) value += 90;
      if (description.includes(token)) value += 35;
      if (text.includes(token)) value += 18;
      if (path.includes(token)) value += 10;
    }
    return value;
  };

  const render = () => {
    const raw = input.value.trim();
    const query = normalize(raw);
    if (!raw) {
      results.innerHTML = '';
      if (status) status.textContent = loading ? 'Loading the wiki index…' : `${index.length} searchable pages indexed`;
      return;
    }

    const tokens = query.split(/\s+/).filter((token) => token.length > 1);
    const matches = index
      .map((item) => ({ item, score: score(item, query, tokens) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title))
      .slice(0, 80);

    if (status) status.textContent = `${matches.length} result${matches.length === 1 ? '' : 's'} for “${raw}”`;
    results.innerHTML = matches.length
      ? matches.map(({ item }) => `<a class="result" href="${escapeHtml(item.url)}"><strong>${escapeHtml(item.title || item.path)}</strong><small>${escapeHtml(item.description || item.path)}</small><span>${escapeHtml(excerpt(item.text, raw))}</span></a>`).join('')
      : '<div class="no-results">Nothing matched that term yet. Try a character, skill, quest number, reward, mechanic, DLC name, or gameplay keyword.</div>';
  };

  fetch('/Dragon-Ball-Xenoverse-2-Wiki/search-data.json', { cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error(`Search index returned ${response.status}`);
      return response.json();
    })
    .then((data) => {
      index = Array.isArray(data) ? data : [];
      loading = false;
      render();
    })
    .catch(() => {
      loading = false;
      if (status) status.textContent = 'Search index could not be loaded.';
    });

  input.addEventListener('input', render);
  input.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      input.value = '';
      render();
    }
  });
})();
