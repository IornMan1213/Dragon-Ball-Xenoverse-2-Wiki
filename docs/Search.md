---
layout: wiki
title: Search Everything
description: Search the entire published wiki by character, skill, quest, reward, mechanic, DLC, guide topic, or any other term.
permalink: /Search/
---

<div class="search-page">
  <div class="search-hero">
    <p class="eyebrow">FULL-TEXT WIKI SEARCH</p>
    <h2>Find anything.</h2>
    <p>Search across every published wiki page. Use a broad term such as <strong>Ki</strong>, <strong>Goku</strong>, <strong>Time Patrol</strong>, <strong>Ultimate Finish</strong>, or <strong>Parallel Quest</strong> and the results will surface pages that actually discuss it.</p>
    <label class="search-box" for="wiki-search-input">
      <span aria-hidden="true">🔎</span>
      <input id="wiki-search-input" data-wiki-search type="search" autocomplete="off" placeholder="Search characters, skills, missions, rewards, mechanics…" aria-describedby="search-status">
    </label>
    <p id="search-status" class="search-status" data-search-status>Loading the wiki index…</p>
  </div>

  <div class="search-results" data-search-results aria-live="polite"></div>
</div>
