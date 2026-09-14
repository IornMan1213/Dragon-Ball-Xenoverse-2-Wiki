const categoryMeta = {
  "Ki Blast Supers": ["Super", "Ki Blast"],
  "Strike Supers": ["Super", "Strike"],
  "Ki Blast Ultimates": ["Ultimate", "Ki Blast"],
  "Strike Ultimates": ["Ultimate", "Strike"],
  "Other Supers": ["Super", "Other"],
  "Power Up Supers": ["Super", "Power Up"],
  "Ki Blast Evasives": ["Evasive", "Ki Blast"],
  "Strike Evasives": ["Evasive", "Strike"],
  "Other Evasives": ["Evasive", "Other"],
  "Power Up Evasives": ["Evasive", "Power Up"],
  "Other Ultimates": ["Ultimate", "Other"],
  "Saiyan Skills": ["Awoken", "Race"],
  "Majin Skills": ["Awoken", "Race"],
  "Namekian Skills": ["Awoken", "Race"],
  "Frieza Race Skills": ["Awoken", "Race"],
  "Human Skills": ["Awoken", "Race"],
  "Unavailable for CaC": ["Mixed", "Special"]
};

const categoryUrls = Object.fromEntries(Object.keys(categoryMeta).map(name => [
  name,
  `https://dbxv2.fandom.com/wiki/Category:${name.replaceAll(" ", "_")}`
]));

const catBox = document.querySelector('#categories');
const recBox = document.querySelector('#records');
const q = document.querySelector('#skillSearch');
const type = document.querySelector('#typeFilter');
const sub = document.querySelector('#subFilter');

function render(data) {
  const term = (q?.value || '').toLowerCase().trim();
  const tf = type?.value || '';
  const sf = sub?.value || '';
  const categories = Object.entries(data.category_counts || {})
    .map(([name, count]) => ({ name, count, ...(categoryMeta[name] || ['Mixed', 'Other']) }))
    .filter(c => (!tf || c[0] === tf) && (!sf || c[1] === sf) && (!term || `${c.name} ${c[0]} ${c[1]}`.toLowerCase().includes(term)));

  catBox.innerHTML = categories.map(c => `
    <a class="db-card" href="${categoryUrls[c.name] || '#'}" target="_blank" rel="noopener">
      <span class="count">${c[0]} • ${c[1]} • ${c.count} INDEXED</span>
      <h3>${c.name}</h3>
      <p>Open the source category and continue into individual skill pages.</p>
      <b>Browse source →</b>
    </a>`).join('');

  const records = (data.records || []).filter(r =>
    (!tf || r.class === tf) &&
    (!sf || r.subcategory === sf) &&
    (!term || Object.values(r).join(' ').toLowerCase().includes(term))
  );

  recBox.innerHTML = records.length ? records.map(r => `
    <div class="seed-row">
      <b>${r.name}</b>
      <span>${r.class} / ${r.subcategory}${r.race_restriction ? ` / ${r.race_restriction}` : ''}</span>
      <small>${r.verification_status}</small>
    </div>`).join('') : '<div class="seed-row"><b>No records matched.</b><small>Try clearing one of the filters.</small></div>';
}

async function boot() {
  try {
    const response = await fetch('data/skills.json', { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    render(await response.json());
  } catch (error) {
    catBox.innerHTML = '<div class="db-card"><h3>Database unavailable</h3><p>The canonical JSON file could not be loaded. The source links remain available in the repository.</p></div>';
    console.error('Skills database load failed:', error);
  }
}

[q, type, sub].filter(Boolean).forEach(x => x.addEventListener('input', () => window.__skillsData && render(window.__skillsData)));

fetch('data/skills.json', { cache: 'no-store' })
  .then(r => r.ok ? r.json() : Promise.reject(new Error(`HTTP ${r.status}`)))
  .then(data => { window.__skillsData = data; render(data); })
  .catch(() => boot());
