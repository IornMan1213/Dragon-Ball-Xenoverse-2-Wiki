const categoryMeta = {
  "Ki Blast Supers": ["Super", "Ki Blast"], "Strike Supers": ["Super", "Strike"],
  "Ki Blast Ultimates": ["Ultimate", "Ki Blast"], "Strike Ultimates": ["Ultimate", "Strike"],
  "Other Supers": ["Super", "Other"], "Power Up Supers": ["Super", "Power Up"],
  "Ki Blast Evasives": ["Evasive", "Ki Blast"], "Strike Evasives": ["Evasive", "Strike"],
  "Other Evasives": ["Evasive", "Other"], "Power Up Evasives": ["Evasive", "Power Up"],
  "Other Ultimates": ["Ultimate", "Other"], "Saiyan Skills": ["Awoken", "Race"],
  "Majin Skills": ["Awoken", "Race"], "Namekian Skills": ["Awoken", "Race"],
  "Frieza Race Skills": ["Awoken", "Race"], "Human Skills": ["Awoken", "Race"],
  "Unavailable for CaC": ["Mixed", "Special"]
};
const categoryUrls = Object.fromEntries(Object.keys(categoryMeta).map(name => [name, `https://dbxv2.fandom.com/wiki/Category:${name.replaceAll(" ", "_")}`]));
const catBox = document.querySelector('#categories'), recBox = document.querySelector('#records');
const q = document.querySelector('#skillSearch'), type = document.querySelector('#typeFilter'), sub = document.querySelector('#subFilter');

function render(data, verified = []) {
  const term = (q?.value || '').toLowerCase().trim(), tf = type?.value || '', sf = sub?.value || '';
  const categories = Object.entries(data.category_counts || {}).map(([name, count]) => ({ name, count, ...(categoryMeta[name] || ['Mixed','Other']) }))
    .filter(c => (!tf || c[0] === tf) && (!sf || c[1] === sf) && (!term || `${c.name} ${c[0]} ${c[1]}`.toLowerCase().includes(term)));
  catBox.innerHTML = categories.map(c => `<a class="db-card" href="${categoryUrls[c.name] || '#'}" target="_blank" rel="noopener"><span class="count">${c[0]} • ${c[1]} • ${c.count} INDEXED</span><h3>${c.name}</h3><p>Open the source category and continue into individual skill pages.</p><b>Browse source →</b></a>`).join('');
  const all = [...(data.records || []), ...verified].reduce((map, r) => { map.set(`${r.name}|${r.class}|${r.subcategory}`, r); return map; }, new Map());
  const records = [...all.values()].filter(r => (!tf || r.class === tf) && (!sf || r.subcategory === sf) && (!term || Object.values(r).join(' ').toLowerCase().includes(term)));
  recBox.innerHTML = records.length ? records.map(r => `<div class="seed-row"><b>${r.name}</b><span>${r.class} / ${r.subcategory}${r.race_restriction ? ` / ${r.race_restriction}` : ''}${r.unlock_method ? ` — ${r.unlock_method}` : ''}</span><small>${r.verification_status}</small></div>`).join('') : '<div class="seed-row"><b>No records matched.</b><small>Try clearing one of the filters.</small></div>';
}

Promise.all([fetch('data/skills.json', {cache:'no-store'}).then(r => r.json()), fetch('data/verified-skills.json', {cache:'no-store'}).then(r => r.json())])
  .then(([data, verified]) => { window.__skillsData = data; window.__verifiedSkills = verified.records || []; render(data, window.__verifiedSkills); })
  .catch(error => { catBox.innerHTML = '<div class="db-card"><h3>Database unavailable</h3><p>The canonical skill data could not be loaded.</p></div>'; console.error(error); });

[q, type, sub].filter(Boolean).forEach(x => x.addEventListener('input', () => window.__skillsData && render(window.__skillsData, window.__verifiedSkills || [])));
