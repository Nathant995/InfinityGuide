# Infinity Guide — DragonInfinity

A complete static guide for RuneScape: Dragonwilds, hosted by S3RVNetwork (part of S3rvStudios).

## Publish on GitHub Pages

1. Extract this ZIP.
2. Create or open your GitHub repository.
3. Upload the **contents of the InfinityGuide folder** to the repository root. `index.html` must be at the top level, alongside `assets`, `.nojekyll` and the other HTML files. Do not upload the ZIP as the website.
4. Commit to your main branch.
5. Open **Settings → Pages → Build and deployment**.
6. Choose **Deploy from a branch**, then **main** and **/(root)**. Save.
7. Wait for the Pages deployment to finish. Open the URL shown by GitHub.

No npm install, build command, API key, server process or database is needed. All paths are relative, so the site supports a repository subpath such as `https://name.github.io/infinity-guide/` as well as a custom domain.

GitHub documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Privacy and the included password

At the host's explicit request, this edition includes the supplied server password **RSDW**, including the original password screenshot. The site is intended for a private audience, but this static package **does not enforce authentication**. A private GitHub repository does not by itself make a Pages site private. Confirm visitor access controls with your hosting arrangement before uploading. `noindex,nofollow` asks search engines not to index the pages; it is not access control. Do not use a client-side JavaScript password prompt as protection for these files.

The password appears in generated `connect.html`, `assets/search-index.js`, `source/content.py`, this README, and `assets/media/HowToEnterPassword.png`. If changing or removing it, update all relevant content and replace/remove the screenshot, then regenerate. Previously published credentials should be rotated rather than relying on deletion.

## Preview locally

Open `index.html` directly for a quick preview. Search and navigation work without a build; local storage and clipboard behaviour can vary on file URLs.

For a more realistic preview, run from this folder:

```sh
python -m http.server 8000
```

Then visit http://localhost:8000 . On Windows, `py -m http.server 8000` is an alternative.

## Included features

- Welcome page plus 19 guide/reference pages and a 404 page.
- All requested guide categories, plus basecamp route, magic, server etiquette, glossary, troubleshooting and credits.
- Full-text local search, including helpful no-result handling and a wiki search link.
- Desktop navigation and mobile menu; per-guide contents links.
- Saved guides, read status and persistent checklists stored in the visitor's browser.
- Filterable controls, skills, resource and glossary references.
- Click-to-enlarge screenshots, keyboard-accessible dialogs, light/dark themes and print styles.
- 2026/2027 roadmap summary clearly separated from released content.
- 19 original host-provided PNG screenshots, with no remote runtime assets or external font dependency.
- Per-guide wiki topic links and relevant Jagex references.

## Edit and maintain

The website is already generated. You can edit HTML directly, but the recommended maintenance route is:

1. Edit `source/content.py` for guide text, links, checklists and image captions.
2. Edit `source/build.py` for the shared layout or homepage.
3. Edit `assets/style.css` for design and `assets/app.js` for interactions.
4. Run `python source/build.py` (or `py source/build.py` on Windows).
5. Upload the changed files, including the regenerated `assets/search-index.js`.

The generator uses Python's standard library only. It does not fetch anything from the internet. Regenerating overwrites the HTML files and search index, so avoid mixing direct HTML changes with source changes.

To change the camp route, replace `assets/media/HowToGetToClanVillage.png` and update its description and route instructions. To change the hero, edit the `.hero` background in `assets/style.css`. The current hero uses the supplied woodcutting screenshot through CSS; the original screenshot is unchanged.

Update dates are manual. The site does not fetch server status, wiki updates or Jagex news automatically. Check the official sources after major patches. Settings shown in screenshots are historical examples, not live information. Quest and boss pages are beginner guidance and directories, not an exhaustive database of every quest step or encounter phase.

## Attribution and source limitations

Reviewed 9 October 2026. Original instructional writing with factual references linked in each guide and `sources.html`. The official wiki restricted direct automated access during preparation, so its linked topic pages were not all live-verified. Jagex help articles and current release announcements supplied the primary gameplay references. In-game tooltips and later patch notes take priority over older guide text.

Screenshots were provided in `RSDW_InfinityGuide.zip`; underlying game content remains the property of its respective owners, including Jagex. No wiki text or wiki artwork is mirrored in this package. Infinity Guide is an independent community resource, not an official Jagex product. No broad licence to Jagex assets is implied.

## Expanded guide library (October 2026)

This edition adds 37 wiki-informed guides across quest walkthroughs, stations, skills, lore and core systems, alongside the original 19 field guides. The home page now includes an expandable topic directory. Search indexes all 56 articles and the offline pages link to the corresponding Dragonwilds wiki entry for full live requirements.

### Rebuilding after edits

Edit `source/content.py` for the original field guides and `source/expand.py` for the topic library, then run:

```sh
python source/build.py
python source/validate.py
```

`source/expand.py` reads the original saved wiki HTML only when generating the site. The prebuilt HTML files already work on GitHub Pages, so you do not need the supplied `WikiPages.zip` to deploy. To regenerate the 37 topic guides, keep the extracted wiki HTML in a sibling folder named `wiki` next to `InfinityGuide` and install `beautifulsoup4` in your local Python environment. Otherwise, deploy the already-generated HTML files without running the build script.

The new deep dives are introductory summaries and task checklists, not exhaustive transcripts of each official wiki page. Follow their source links for comprehensive requirements and quest solutions.
