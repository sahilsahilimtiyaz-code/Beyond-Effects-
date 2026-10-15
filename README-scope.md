# Beyond Effects — overlay set (scope note)

This repository revision contains ONLY:

- `overlay-8c/` — staged home-screen layout overlay (1 file).
- `overlay-8d/` — staged launcher-icon art, adaptive-XML reference copies, and
  the generator script (provenance).
- `overlay-fx/` — custom-effect payloads, byte-identical to phase pins (2P
  letterbox, 2X bloom saturation+, 6B bloom region+; thumbs renamed to packaged
  `assets/thumb/<name>.png` per `thumb=` attrs, 2N precedent).
- `overlay-8e/` — display-path corrections (root-cause fix for unchanged installs):
  `gold_motion_launcher.png` (576², manifest `icon`/`roundIcon` live path) +
  `gold_motion_logo_splash.png` (1024², splash-theme live path) + generator
  provenance. Replaces same-path originals only; no XML/manifest/smali touched.
- `overlay-8f/` — onboarding rebrand (literal-only smali edits, exact class/method
  traced): `GoldStartupActivity` + `$3/$5/$5$3/$6/$6$4` — crimson primary buttons
  + progress tints, near-white headlines/status/button text, Beyond Effects
  headlines. No structural, id, manifest, or navigation changes.
- `overlay-9a/` — Octavian identity + loading + promo-source (additive branch work):
  edited `AndroidManifest.xml` (package `com.octavian`, 12 authorities, permission,
  4 Octavian labels), `res/xml/dev_preferences.xml` intent, 4 renamed smali
  authority literals, `GoldStartupActivity` loading sequence (`showLoading` + `$9`
  ticker, onboarding screens bypassed, engine-gated via `GmFxStatus`), `WelcomeDialog.show()`
  disabled at entry. Smali pre-verified with pinned smali-2.5.2.
- `overlay-9b/` — Beyond identity on live paths: launch-mark text
  (`StudioLaunch`: `B E Y O N D   E F F E C T S`), crimson launch ring
  (`StudioLaunch$Mark`), drawer follow row removed (`snsHolder → gone` in
  `project_list_sidemenu_header.xml`). Manifest labels now `Beyond Effects`
  (package stays `com.octavian`).
  Drawer brand block: B icon + `Beyond Effects` title + crimson divider inserted
  at the top of the drawer header (new `@+id/beBrand*` hierarchy; sns row stays
  gone; settings/menu content untouched).
- `overlay-9d/` — editor shell slice B (live `MainActivity` path via `GmUiFixes`):
  crimson topBar divider, guaranteed `Beyond Effects` wordmark, graphite topBar,
  whitened export/cover holders. All null-safe `find()`-based, no structural edits.
- `overlay-9e/` — app-wide palette restyle (scripted, 25 gold→crimson token remaps,
  hue-rotated at constant lightness/saturation/alpha; functional hues, SDK colors,
  and effect-viz groups untouched; everything else byte-identical).
- `overlay-9f/` — storage discipline + update-popup removal: `GMBackup`
  never redirects to all-files settings (MediaStore backup path kept; manifest
  `MANAGE_EXTERNAL_STORAGE` line removed after tracing sole-consumer +
  fallback); `ForceUpdateManager` fetch + dialog-show disabled at source
  (server-gated promo/update dialog can no longer trigger). Twin-dex copies in
  `smali_classes24` (which win at runtime) patched identically.
- `overlay-9g/` — workspace rebrand: `app_name` → Beyond Effects (8 layouts),
  page brand/tabline/select-all gold → crimson. Tag/id contract untouched.
- `overlay-9h/` — action surfaces: CREATE button, new-project FAB, and
  multi-select bar gold → crimson (pressed state darker). Shapes, states,
  radii, and users (creation/workspace only) unchanged.
- `overlay-9j/` — home dashboard + promo purge (traced live path
  `PerformanceInitProvider` → `GmUiFixes.install` → `apply` → `StudioAppearance`
  → `find`, plus `CustomizationManager.visit` prefs styling): home hero
  152dp centered emblem → compact left-aligned 72dp dashboard header
  (title 27→22sp, "Motion, reimagined." caption, crimson rules); promo
  `bindLink` calls + fwpnkj/Telegram URLs deleted at source; drawer sns block
  (Follow me/Instagram/Telegram) removed from layout; 68 display strings
  rebranded (7 legal/factual exclusions kept); `CustomizationActivity`
  defaults + screen title rebranded. All IDs/types preserved; greeting,
  profile, title/tagline, customize-link and settings rows functional.
- `overlay-9k/` — loading compact: `setup_overlay` caption removed, emblem
  108→96dp, tighter spacing. Startup engine screen (`showLoading` + codec
  ticker) and launch panel verified button-free; no fake delays added.
- `overlay-9l/` — effects browser header (verified live via `hoy/BXT`
  binding): 52→78dp two-line header (title 18sp + new subtitle string),
  vertically centered controls, charcoal surface. All IDs/types, fragment
  holders, listeners and search preserved.
- `overlay-9m/` — promo-dialog purge (PROMO-GONE gate found the last dex
  copies): `zenapp Customdialog` welcome text → Beyond Effects, fwpnkj +
  Aftermotionex Telegram handles stripped (9 intents kept well-formed);
  disguised `support/annotation/B` "Follow @fwpnkj" → Beyond Effects.
  Reachability trace pending; texts neutralized at source regardless.
- `overlay-9n/` — follow-toast trigger removed: `MainActivity.onResume`
  called disguised `B.mod` (custom "Follow @fwpnkj" toast over home on every
  resume; toast-only, no functional side effects). Single straight-line call
  deleted; resume flow otherwise byte-identical.
- `overlay-10a/` — editor cockpit (native `onCreate` boundary documented;
  bars are native-inflated by ID so order/geometry/tint edits are safe, but
  no IDs/types/visibilities changed): playbar regrouped transport-first
  with prominent Play (1.6 weight); actionbar Close-first; navbar/selectbar
  42→48dp with 44dp targets, gold tints → white; play/info bars 46→52dp;
  timeline rows 30→34dp (`TimelineLayoutManager` reads the attr).
- `overlay-10b/` — home Continue card on real data: new public
  `GmProjectsPage` accessors (`recentCount/Title/Meta`, `thumbRecent`,
  `openRecent` via public `MainActivity.UG`, `ensureLoaded`); `StudioAppearance`
  injects thumb + title + meta card opening the actual project, or a clean
  empty hint while the stock lister is cold. No fake projects/thumbnails.
- `overlay-10c/` — effect rows grip-leading (drag, name, badges, visibility,
  expand). IDs preserved; adapter untouched.
- `overlay-11a/` — dead-code URL strip: `MainActivity$GoldTelegramClickListener`
  (zero instantiators in any dex; keeps well-formed `https://t.me/`).
- **BISECT 2026-10-15**: run `38694780463` (incl. 10A/10B/10C) crashes at tap
  on Galaxy A54. `10A/10B/10C` unwired in workflow (overlay dirs retained);
  build output is `0a45c35`-equivalent. Static analysis: none of the 10x code
  executes before MainActivity, and the 10B call sits behind a gate that
  returns before reaching it — regression unproven, bisect artifact decides.
- **FIX 2026-10-15 (VerifyError)**: device log proved `StudioAppearance.apply`
  failed ART verification (v2/v3 Undefined after 9J promo deletion) → whole
  class rejected at launch. Fixed with empty-string register stubs (commit
  `7d8be10`); `PROMO-GONE` still green.
- **FIX 2026-10-15 (binding IDs)**: device log proved `hoy.MC` binding mandates
  the drawer promo IDs I deleted (`Missing required view: followUs`) →
  promo block restored present-but-`gone` with labels stripped (no listeners
  attached). New CI `ID-CONTRACT` gate fails the build if any overlay layout
  drops an ID the pristine layout has. Rule: hide, never delete, ID'd views.
  build output is `0a45c35`-equivalent. Static analysis: none of the 10x code
  executes before MainActivity, and the 10B call sits behind a gate that
  returns before reaching it — regression unproven, bisect artifact decides.
- `overlay-9i/` — gallery card redesign (traced live path `GmProjectsPage`
  `render` → `cols` → `card`; dead `listitem_project_list.xml` untouched):
  thumbs 16:9 → 4:3, grid gap 13 → 16dp, card radius 13 → 18dp,
  title 12.5 → 14sp / meta 11 → 12sp with looser margins, duration pill
  10.5 → 11.5sp, check 22 → 26dp, overflow 26x22 → 30x26dp,
  list thumb 64 → 80dp, section headers 11 → 12sp. No view added/removed;
  open, long-press select, overflow menu, search, sort, and export callbacks
  byte-identical.
- `overlay-9c/` — workspace slice A: home-stage follow block removed at its source
  (`StudioAppearance.apply`: `FOLLOW ME` + Instagram/Telegram rows never built;
  workspace-link row, prefs toggles, and settings screen preserved).
- `.github/workflows/canary.yml` — toolchain canary (manual trigger, no secrets,
  no APK build).
- `.github/workflows/rebuild.yml` — APK reconstruction (manual trigger; original
  APK supplied at run time via URL+SHA, never committed; in-run throwaway test
  key only).
- `pins.md`, `.gitignore`, this note.

It does NOT contain: the original APK, decompiled sources, DEX, native
libraries, shipped assets, signing keys, backups, logs, or intermediates.
Reconstruction work stays disabled until separately approved.
