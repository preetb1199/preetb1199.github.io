# Publish Preet Baxi's AI + LIGO research portfolio

This ZIP is **the complete source code** for the current website. Its files are intended to sit at the *root* of a GitHub Pages repository, not within a nested portfolio folder.

## 1. Create or open your GitHub Pages repository

- GitHub account: `preetb1199`
- Repository name: `preetb1199.github.io`
- Repository visibility: public
- If this repository already exists, update its files rather than creating a duplicate.

## 2. Upload the website

1. Extract the ZIP on your computer.
2. Open the repository on GitHub.
3. Select **Add file → Upload files**. Upload **the contents** of the extracted ZIP, keeping the `assets/` and `research/` folder structures. GitHub's browser upload may need drag-and-drop of the entire contents; using Git locally is another option.
4. Commit changes to `main`.

Expected repository root:

```
.nojekyll
index.html
publications.html
README.md
PUBLISHING.md
assets/
  styles.css
  site.js
  portrait.webp
  Preet_Baxi_CV.pdf
  favicon.svg
  diagrams/
  thumbs/
research/
  index.html
  agentsentry.html
  metaaudit.html
  ligo-monitoring.html
  ...other project pages
```

## 3. Turn on GitHub Pages

In repository **Settings → Pages**, choose **Deploy from a branch**, then `main` and `/(root)`, and save. Once GitHub deploys the site, it will be at:

https://preetb1199.github.io/

## 4. Optional custom domain

You can later configure `www.preet-baxi.com` under **Settings → Pages → Custom domain** and follow GitHub's DNS directions. Do not add a `CNAME` file until your DNS is set up correctly and you're ready to use the domain.

## Notes

- `index.html` uses `assets/styles.css` and `assets/site.js`, so keep those files together.
- Research detail pages load CSS/JS via `../assets/...`.
- Do not upload the ZIP as a single file or copy only `index.html`.
- Interactive research elements are educational UI explainers, not live model or security monitoring services.
- Before a public launch, review paper citations and experiment statistics against your final CV/manuscripts.
