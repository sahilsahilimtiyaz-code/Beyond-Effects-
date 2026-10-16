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
- `overlay-12a/` — editor stage + add panel (Stage 3 slice 1; native panel
  switching untouched, no tab/list reordering since native may index children):
  add-panel strip/rail 58→64dp with 10sp labels, gold active states →
  shared `be_tab_state` crimson component, light tile neutralized; preview
  stage 8dp charcoal frame, playhead zone 120×44, overflow 44dp with margins,
  viewmode rail 56dp. All IDs/types/parents/visibilities preserved.
- `overlay-13a/` — creation form hierarchy (header title + subtitle above the
  type segment, 68dp aspect targets) + effect category `PNKJ` → `BEYOND` +
  welcome-copy fix. New strings additive; `zNr` IDs preserved.
- CI now proves APK contents: `aapt2 dump xmltree` markers for create/effects/
  add-panel/homefeed + dex markers for the injected home code.
- `overlay-14a/14b` — library header reorganization + runtime-logo source fix:
  toolbar merged to one 56dp row (menu, title+count, search, view toggle;
  all 36 `gm*` tags preserved, none deleted/renamed), and the
  runtime-injected workspace logo killed at its source — `brandLogo()` loads
  `assets/GOLDMOTION.png`, so the asset is now a transparent 1×1 (decodes
  fine, slot collapses, zero branding, zero code change).
- `overlay-15a/` — timeline/search refinement: `timeline_row_height` 30→34dp
  aligned with `TimelineLayoutManager` (fixes 10A mismatch); static red
  layer-type strip → neutral (native never recolors it); visibility toggle
  40dp; search header 52dp charcoal zone with centered back action.
  Export strings verified honest (failure + storage guidance, no fake success).
- `overlay-18a/` + drawer sections — export action hierarchy (SAVE full-width
  primary; SHARE + Close secondary row) and drawer recomposition (WORKSPACE /
  SUPPORT / DEVELOPER section headers with re-chained constraints; promo block
  untouched-gone). All IDs preserved; progress honesty untouched.
- `overlay-19a/` — editor viewmode recomposition: 56dp vertical edge strip →
  full-width 52dp horizontal canvas-tool strip under the navbar (pixel/grid/
  solo/camera + canvas zoom re-chained; preview and floating guides follow);
  effect grid cards 80→84dp with 11sp names. All IDs/types/parents kept.
- `overlay-20a/` — real tab navigation mapped: nav taps route
  `Click(index)` → `pick()` (2→create sheet, else `uRg(Mk)` tab select;
  index 1 = Projects, same call the nav button makes). Home empty state is
  now tappable via `pick(activity, 1)` — no invented API. Bottom-nav
  constraint closed.
- `overlay-17a/` — inspector + settings: shared `be_inspector_label_text`
  mint active/pressed states across all 7 property rows, slider thumb 18→22dp
  for precise scrubbing, preferences grouped into 3 labeled categories
  (keys/defaults untouched). Bottom-nav mapping: tab switching lives in
  Compose/native (`GmNavBar.sync` drives; no MainActivity select-tab API) —
  documented open, no fake wiring.
- `overlay-16a/` — effects/export/nav refinement: mint create disc; detail
  panel hierarchy (36dp overlap, 22sp title); recommend density; export SAVE
  primary (1.4 weight, honest spinner/progress kept); drawer social labels
  fully stripped (gone block, no listeners). Layer-tag verified static
  (zero adapter refs — native never sets it, neutral default correct).
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
- `overlay-21a/` — layer action bar 42→48dp with 44dp targets; transform
  numeric chips 63×25→68×30 with 7sp axis labels, mint active states,
  widened XY holder. Native gesture pads, spinners, link toggles untouched.
- `overlay-23a/` — transport integration: the floating Add button moves into
  the playbar chain first ([Add][transport][undo/redo][layers][preview]),
  freeing the timeline corner; add sheet 251→300dp. Union ID-contract holds
  (buttonAdd lives in the playbar include within the same tree).
- `overlay-24a/` — preview/timeline rebalance: timeline 280→240dp gives the
  stage +40dp (RecyclerView adapts; rows/manager/dimen agree at 34/240);
  timeline overflow moves off the layer-header corner to the trailing corner.
- `overlay-26a/` — cockpit delegation (mockup-faithful where real): navbar
  [back][title][undo][redo][settings][Export pill] with share kept gone for
  the binding; timecode docked in transport; left tool rail
  (Media/Templates/Audio/Text) over the stage edge. Every new control
  delegates via performClick to the existing working control (no invented
  ops); EditActivity wiring via lifecycle hook with null-guards. Declined:
  landscape (portrait-locked manifest+native), AI Tools/snap/grid/keyframe
  bar/fullscreen (no backing ops), colored tracks (native never sets them),
  persistent inspector sliders (needs native panel control), relabeling
  viewmodes with unverified meanings.
- `overlay-27a/` — binding-include rule (from device crash: `hoy.Q8S` binds
  the navbar include subtree, so moved IDs crash native inflate):
  editTimeView and buttonAdd restored to their native includes; pill,
  undo/redo, and rail kept as pure additions. Rule hardened: IDs never cross
  include boundaries; additions only.
- `overlay-28a/` — AI Tools rail entry (real engines verified: AITwixtorEngine,
  AiUpscaleEngine, AudioConverterPanel): 5th rail button with original sparkle
  icon launches ToolStudioActivity via the app's own intent pattern
  (`gold_tool` extra); studio title chrome rebranded, functional help copy
  untouched. Portrait-safe activity; back returns to editor.
- `overlay-29a/` — rail robustness: sheet+tab rail buttons check addPopup
  visibility first (no double-toggle when the sheet is already open), then
  fire the real tab control. Every new button audited end-to-end against an
  existing working target; null-guarded throughout.
- `overlay-30a/` — runtime themer fix (from device screenshot): the mod's
  `CustomizationManager$1` repainted editor icons/home with hardcoded GOLD
  defaults (#FFF2C94C accent, Gold Motion/MOTION DESIGN titles) on every
  launch, overriding all XML work — defaults now mockup-blue/Beyond.
  Plus: layout-guarded editor wiring (fires post-layout when views exist),
  compact centered rail (frees canvas), white eye icon, tap-diagnostic
  toasts naming the fired control (temporary, removable).
- `overlay-31a/` — Elements rail entry via the proven sheet+tab delegation
  (object tab). Layers entry declined: no global layers destination exists.
  Effects entry pending launcher trace.
- `overlay-32a/` + 9N-surgical — user punchlist: 69 gold drawables mapped by
  role (active→mockup blue, neutral→white; warnings/errors/system untouched),
  dev header blue, library transparent underlines blue, dead Telegram URL
  strings stripped (4 files), support emails → sahilsahilimtiyaz@gmail.com,
  Help Centre row gone (binding ID kept), follow-toast trigger deleted with
  a one-line surgical CI patch (no whole-file copy), add-sheet gets a real
  toggle handle wired to the working Add button, missing letterbox thumb
  generated as a "GL" letter badge per the requested fallback.
- `overlay-33a/` — mockup-faithful home composition: glass brand card
  (emblem + title stack + chevron, tappable to library), 56dp New Project
  pill with plus icon, "No recent projects" titled empty section (tappable),
  pink dash. Fixed shipped bug: the library tap listener had landed on the
  New Project button (now restored) instead of the empty hint.
- `overlay-34a/` — mockup home details: two-tone greeting (name in export
  pink via ForegroundColorSpan at the real setter; falls back to plain text
  without spaces), code-drawn neon film illustration in the empty state,
  gradient CTA with solid fallback. Subtitle untouched (live engine status),
  bell/nav declined (no notifications feature, Compose-owned).
- `overlay-36a/` — real pixels cropped from the supplied mockups (pure-python
  PNG codec, verified by re-reading each crop): 6 rail icons, neon B mark
  (home emblem + drawer brand), full film illustration (empty state).
  Nav icons already white vectors (kept). Bell declined again: zero backing
  functionality exists to wire it to.
- `overlay-37a/` — gradient play tile (blue→purple→pink, 12dp) on the
  prominent play control. Tool-grid panel declined with proof: target menu
  buttons live in a natively-inflated popup (absent until opened) and no
  duplicate-layer operation exists — grid buttons would be dead.
- `overlay-38a/` — stage chrome: dotted-grid canvas backdrop (tiled,
  shows in letterbox/padding around the native surface), rounded transport
  bar inset from screen edges, blue-ring FAB. Timeline cells verified
  engine-painted (native bg/thumbs/keyframes) — correctly untouched.
- `overlay-39a/` — unified home code: merges the diverged 34a/35a lines
  (illustration, gradient CTA, 56dp pill, empty section, stage tap, guarded
  span) into one StudioAppearance; 28sp greeting, gradient-border glass.
  Supersedes 33a/34a smali copies (34a step now ships only the reverted
  Manager + film art).
- `overlay-40a/` — app-structure pass: dev prefs rebranded (Mod by octavian,
  Beyond AI, fixed Customization target package), collapsible rail via edge
  toggle tab (pure view visibility, zero native interaction), nav bar as
  rounded-top sheet with red plus disc + pink selected tabs, AI-studio gold
  already covered by the drawable sweep (no smali gold in tools code).
  Optimization note: all wiring is one-time at inflation; zero per-frame
  additions; rail/toast views are static.
- `overlay-41a/` — Beyond AI: titles/toasts/manager strings rebranded;
  floating face repainted (blue rim, white eyes, glowing red pupils, blue
  mouth, white shine — zero gold). Twin-dex checked (single copy).
  Contact-support wiring pending drawer-handler trace.
- `overlay-43a/` — labs cube blue (text labels + 3D material default),
  floating-AI toggle row deleted (pref stays false = bubble never shows),
  per-build version stamp (`7.0.3-be<sha>`) + drawer build tag so the
  installed build is always identifiable. Play Protect note: test-key-signed
  sideloads always warn; fixed properly only via Play App Signing.
