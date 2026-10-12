# Infinity Guide — DragonInfinity

Static reference site for RuneScape: Dragonwilds. DragonInfinity is hosted by S3RVNetwork, part of S3rvStudios.

## Publish to GitHub Pages

1. Extract the ZIP.
2. Upload the **contents of the InfinityGuide folder** to your repository root. `index.html`, `assets/` and `.nojekyll` belong at the top level.
3. Commit the files.
4. In the repository's Settings → Pages, choose deployment from your main branch and the root folder.
5. Open the Pages URL when deployment finishes.

No install, database, API key or build command is needed to host the delivered files. Relative links support GitHub project subdirectories. The server password RSDW remains included as requested. This static package does not itself restrict visitor access.

## What's in this edition

- 629 recipe variants across 20 facilities, with exact inputs, output quantities and recorded XP.
- Searchable recipe planner: choose desired output, calculate whole batches and inputs, choose ×1 or ×3 XP, and follow component recipes.
- All level 1–99 cumulative XP thresholds and a target/action calculator.
- Skill unlock tables; ore locations and tool requirements; fishing XP, bait and starter equipment.
- Individual workstation recipe tables, plus Cooking Range food effects.
- A step-by-step stone-to-bronze workshop guide and expanded main-quest walkthroughs.
- PC, Xbox Series X|S, PS5 and Switch 2 control selector, remembered between pages and included in key walkthroughs.
- New host-provided artwork on the landing and overview pages.
- Mobile quick-access navigation, searchable directory, full-text search, saved guides, persistent checklists, themes, image enlargement and print layouts.
- Existing guide URLs retained. Older topic URLs now contain the corresponding detailed reference instead of generic summaries.

## Preview locally

Open `index.html`, or run `python -m http.server 8000` from the InfinityGuide folder and visit http://localhost:8000. On Windows, `py -m http.server 8000` also works. Browser storage and clipboard permissions may differ for local file URLs.

## Editing and rebuilding

The generated HTML is ready to use. If editing the sources:

- `source/content.py`: original guide sections.
- `source/expanded.py`: detailed tutorial, quest, lore and practical references.
- `source/reference.py`: recipe pages, skill tables, XP page, platform controls and legacy page compatibility.
- `source/build.py`: shared layout and landing page.
- `assets/recipes.json`: recipe ingredients, outputs, base XP, food effects and source URLs.
- `assets/references.json`: extracted wiki reference tables.
- `assets/xp-table.json`: cumulative level totals and provenance.
- `assets/app.js`: search, bookmarks, checklists and navigation.
- `assets/reference.js`: platform selection, recipe calculator and XP calculator.
- `assets/style.css`: presentation and responsive layouts.

Run:

```sh
python source/build.py
python source/validate.py
```

Python's standard library is sufficient. Original saved wiki HTML and third-party Python packages are no longer needed to rebuild. The build regenerates HTML, search data and the JavaScript recipe/XP data from the bundled JSON.

## How to interpret the data

Recipe XP is per batch, not per output item. Twenty recipe rows have no numeric XP in the supplied table; these display “Not recorded”, never a made-up zero. A listed zero is retained as zero. The planner counts direct ingredients only; fuel, station construction, station upgrades and component sub-recipes are separate.

The ×3 option is a calculation setting, not a live server query. XP thresholds do not change with XP rate. Food, equipment and potion bonuses are not silently added.

The saved wiki pages disagree about some Woodcutting unlock levels and the pickaxe required for Blurite. These conflicts are explained on the relevant pages. Native controller mappings are distinguished from physical-button equivalents with an asterisk. See `keybinds.html` for source confidence. Switch coverage means Nintendo Switch 2.

The source snapshots are not a live wiki feed. Website checks are not in-game verification. Recipe discovery, station upgrades and patch changes can affect availability.

## Attribution

Recipe data, skill tables and adapted wiki guidance are attributed to RuneScape: Dragonwilds Wiki contributors under CC BY-NC-SA 3.0. The derived wiki content and datasets retain that licence. Every reference guide links its relevant wiki pages; individual recipes include item and source-table links.

The XP table uses the community GEGEBASE Experience reference, which credits the original wiki; milestone totals were checked against runescape-dragonwilds.wiki's XP calculator. Platform controls use Jagex's published keyboard bindings and 1.0 changes, plus the current PS5 layout reported by Spottis. Source URLs and limitations are in `sources.html`.

Screenshots and the new artwork were supplied by the host. Underlying game assets and RuneScape intellectual property belong to their respective owners, including Jagex. The wiki-content licence does not imply ownership of those game assets. Infinity Guide is an independent community site.

See `VALIDATION.md` for the checks performed and `CHANGELOG.md` for this update.
