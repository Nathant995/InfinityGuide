# Validation — reference edition, 12 October 2026

## Passed

- Python generator rebuilt the site from the bundled source and JSON, without the original wiki HTML.
- 82 HTML files validated for local targets, fragment links, duplicate IDs and image alt text.
- 5,073 local references resolved after the content update.
- Chromium browser checks covered all 62 non-alias guide entries at 390px width: no page-level horizontal overflow or JavaScript errors.
- Selected landing, controls, recipe, XP and bronze-workshop pages checked at 320px.
- Desktop landing and recipe tool visually inspected at 1440px; mobile landing and XP layout inspected at 390px.
- Site search, mobile navigation, saved-guide dialog, bookmark/checklist persistence and remembered platform choice exercised.
- Control table switches to the selected platform, with two visible columns.
- Three Bronze Swords calculate 24 Bronze Bars and 540 Artisan XP at ×3.
- From 0 XP to level 99 at 20 base XP/action and ×3, the XP calculator returns 16,667 actions.
- XP dataset contains 99 strictly increasing cumulative totals, starting at 0 and ending at 1,000,000.

## Boundaries

- Browser checks used Linux Chromium, not physical Xbox, PlayStation or Switch hardware.
- Controller-equivalent mappings are labelled where no native platform screenshot was independently verified.
- The source wiki can restrict automated live access. Saved wiki tables supply the recipe and skill datasets; community references supplied and cross-checked the XP curve.
- No live game or server was modified or tested. Deployment was not performed.
- Static validation checks local links; external wiki destinations remain subject to changes and redirects.
