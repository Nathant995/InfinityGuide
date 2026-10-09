# Validation — 9 October 2026

Completed:

- Generated 21 static HTML files: welcome page, 19 guides/reference pages and a 404 page.
- Validated 920 local links/assets and same-site heading fragments with no missing targets.
- Checked unique HTML IDs and screenshot alternative text.
- Verified all 19 supplied PNG files decode correctly and are referenced by the site.
- Passed JavaScript syntax checks for the application and full-text search index.
- Built the site using only Python's standard library; no web build dependency is required for hosting.
- Checked that asset and navigation URLs are relative to support GitHub Pages repository paths.

Limitations:

- Browser-based visual and interaction testing could not be completed in this environment. The local browser dependency could not be installed, and the remote browser could not access the local preview. Responsive layouts and interactions are implemented but are not claimed to have passed end-to-end browser testing.
- External wiki topic pages could not all be checked live due to automated-access restrictions. Jagex source pages were reviewed separately.
- The roadmap is a dated summary, and server settings/passwords require manual maintenance.
- This package provides no visitor authentication. Hosting access controls determine whether it is private.

To repeat the structural check, run `python source/validate.py` from this folder. If Node.js is available, run `node --check assets/app.js` and `node --check assets/search-index.js`.

Before publishing, open `index.html` or serve the folder locally, test a search and a checklist, and view the layout on your phone. Hosting instructions are in README.md.
