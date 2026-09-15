# GitHub Pages

This repository publishes the wiki from `/docs` using the GitHub Pages deployment workflow in `.github/workflows/pages.yml`.

## How publishing works

Every push to `main` triggers the Pages workflow. It builds the Markdown in `/docs` with Jekyll, applies the custom wiki layout and styling, uploads the generated site, and deploys it to GitHub Pages.

The public site is:

**https://iornman1213.github.io/Dragon-Ball-Xenoverse-2-Wiki/**

## Local structure

- `docs/index.md` — public landing page
- `docs/_config.yml` — Jekyll configuration
- `docs/_layouts/home.html` — home page shell
- `docs/_layouts/wiki.html` — article layout and navigation
- `docs/assets/site.css` — site styling and responsive layout
- `docs/*.md` — wiki articles

## Making site changes

For navigation, colors, spacing, typography, cards, mobile behavior, or other visual changes, edit the files above and push to `main`. The deployment workflow handles the build automatically.

Keep the actual wiki content in Markdown. The site layer should improve presentation and navigation without changing the underlying reference material.
