# Beyond Effects — Full Overhaul Blueprint (Phase 1)

Branch: `be/full-overhaul` (forked from known-good `222f9c1`, itself built on
`be/workspace-structural`). Baseline releases retained; nothing force-pushed.
No runtime verification is claimed anywhere without device evidence.

## 1. Screen inventory (78 manifest activities; ~30 app-specific)

### Launch / onboarding — surface: Smali + Compose, risk S
`GoldStartupActivity` (launcher; rewritten 8f/9a — verify-clean), `OnboardingActivity`
+ `OnboardingLauncher`, `OnboardingDoneActivity`, `DeviceMismatchNoticeActivity`,
`setup_overlay` (home cover). Extension points: full (own code). Done except polish.

### Home shell — surface: XML + Compose + programmatic, risk M
`MainActivity` + `activity_home_screen.xml`: 5 tab holders
(`tab_home/projects/templates/ranking/tutorial`), topBar (hamburger, wordmark,
profile, tutorial, account), `ComposeView composableMainContent` (bottom nav
`MainTabsRowKt` — tab-switch API unmapped), holders (cover/create/export/
newFeature), `gm_nav_bar.xml` (Home/Projects/plus/Templates/3D Labs),
drawer = full settings panel (`project_list_sidemenu_header.xml`), NOT a header.
Home tab: `MainTabHomeFeedFragment` + dashboard layout (9j) + injected
Continue/New-Project (10b). Projects tab: Compose `projectTab` + `GmProjectsPage`
programmatic grid (search/sort/select/export/share/duplicate/delete/rename).
Templates/Ranking/Tutorial: Compose + Fragments + rows.

### Creation — surface: XML + binding + Smali, risk M
Plus → `MainBottomSheetKt` → `createProjectHolder` sheet → `LZn`
(`CreateProjectFragment`) + `zNr` binding + `create_project_fragment.xml`
(aspect/resolution/fps/bg/name/type). Tablet `addpopup_large` = DEAD
(zero dex refs — never touch). Remaining: restyle creation form to the
component system; exact sheet-trigger call mapped via `GmNavBar.plus`.

### Editor — surface: XML + bindings + native transactions, risk L (see §3)
`EditActivity` (native `onCreate` + ~300 native stubs; 2 Java bodies).
Binding `hoy/S` + sub-bindings. Chrome: navbar / actionbar / playbar /
infobar / selectbar + select_bottomvar / addPopup (tabs + quick rail +
ViewPager + lists) / preview (`previewGuide` + `SurfaceView previewView`,
`fullScreenPlayer`) / timeline (`RecyclerViewEx` + `TimelineLayoutManager`,
rows `timeline_item/header/grip`) / `elementFragmentHolder` +
`elementLargeFragmentHolder` (20+ property/effect fragments, controls
`effect_setting_*`: slider/color/pos/xyz/spinner/selector/switch/text/
orientation/hue_disc + static tip/section) / layer menus / overflow /
`composableContent` / toasts / guides. Export: `ExportPreviewActivity`
(full XML) + export settings fragment + `SaveToStorageActivity`.

### Effects — surface: XML + fragments, risk M
`EffectBrowserActivity` + `effect_browser_activity.xml` (binding `BXT`),
category/list/detail/search frags, rows (`effect_list_item` reordered 10c,
`effect_item_ver2`, `effect_cate_item`, `effect_recommand_item`,
`effect_search_result_item`), popup (`effect_list_popup`), param panels above.
Engine/serialization untouched by rule.

### Media / import — surface: XML + rows, risk S
`MediaBrowser`, `AudioBrowserActivity` (+ bucket/category/row layouts),
`FontBrowserActivity` (+ rows), `ImportActivity` (SEND/VIEW/*.amproj),
`TemplateImportPreviewActivity` (programmatic), `ElementDownloadActivity`
(WebView), scenebrowser. Mostly row-level restyle work.

### Management / account / monetization — surface: mixed, risk M
Project overflow/menus (programmatic + XML shells), side menus (XML),
`MyAccountActivity` (XML+Compose — JayLibu promo STRIPPED 11a-scope),
settings shells + PreferenceFragments, paywall/survey/creator/ranking
(programmatic/Compose — strings-only surface).

### Tooling — surface: programmatic, risk S (strings/theming only)
`CustomizationActivity` (defaults rebranded), `ToolStudioActivity`,
`YtvdBridgeActivity`, `GoldAiActivity`, tutorial (XML), about (XML),
color picker (XML + custom views), export preview (XML).

## 2. Navigation map
Startup → profile/onboarding gate → engine eval → MainActivity
[Home | Projects | Templates | Ranking | Tutorial ‖ plus-sheet ‖ drawer]
→ EditActivity [preview ‖ playbar ‖ timeline ‖ add-panel ‖ property/effect
holders ‖ layer menus ‖ export] / browsers / account / settings.
All dialog/menu/panel switches preserved; back-stack untouched.

## 3. Boundaries (verified, not assumed)
- Native: render/codec `.so` only; `EditActivity` lifecycle + fragment
  transactions + adapter wiring + Surface callbacks + export launchers.
- Bindings (`hoy/*`, incl. `MC`, `S`, `BXT`, `zNr`): generated against
  ORIGINAL layouts — every original `android:id` must exist with the same
  view type (CI `ID-CONTRACT` gate enforces). Extra views allowed.
- ART verifier: whole-method verification — smali deletions must leave all
  registers defined on every path (lesson: 9J VerifyError). No tab/list
  reordering where native may index children (add-panel tabs, rail).
- Twin-dex: `smali_classes24` wins over `25` for duplicated classes —
  patch both or verify single-copy (lesson recorded).
- Dead layouts (zero dex refs): `activity_project_list_main`,
  `activity_project_list_addpopup_large`, `listitem_project_list` — excluded.

## 4. Component system — DESIGN TOKENS v2 (master brief)
Background `#090B0D`, base `#111519`, raised `#191F25`, elevated `#222A32`.
Primary text `#F2F5F7`, secondary `#B2BDC7`.
Primary accent **mint `#62E5BA`** (12.6:1 on near-black, computed),
pressed `#35B184` (7.3:1), med `#7DE9C6`, pale `#C9F5E3`, deep `#1E8A62`.
Accent foreground (text/badges ON mint) `#062319` (10.7:1, computed).
Never white-on-mint (1.6:1). Crimson fully migrated out (commit on
`be/full-overhaul`; 25 palette tokens + 15 flat refs + smali consts).
Semantic reds (errors, declines, system palettes) intentionally untouched.
Shared components: `be_tab_state` (activated-tab state list), card radius
via `StudioAppearance.card` (pref `studio_radius` dp 24), `gm_create_*`
field/section drawables, `spacegrotesk/roboto` type scale (title 22/18/15,
body 12/11, micro 10). Honors `studio_reduce_motion` pref (no decorative
choreography). 44–48dp touch targets on bars/buttons.

## 5. Screen-by-screen plan (Phase 2 queue)
1. Promo sweep completion (S): Telegram listener (done 11a), JayLibu/MOD-by
   (done), drawer permanent removal (needs binding-safe replacement view —
   design: `gone` stays until a same-ID stub layout ships), banner strings.
2. Home/library (M): Continue + New Project shipped (10b, needs device
   verdict); next: projects-tab header row + empty-state polish.
3. Creation form (S): restyle to components; keep `zNr` IDs + `LZn` flow.
4. Editor cockpit (L): 10A+12A shipped (verdict pending); next: add-panel
   content hierarchy + property-row standardization (`effect_setting_*`
   label/value/keyframe order + shared section headers).
5. Effects depth (M): category/detail/search frag layouts + param grouping.
6. Browsers/export/menus (S-M): row standardization, export settings +
   progress states, layer menus, bottom sheets.
7. Consolidation (S): strings audit, dead-string removal (non-functional
   only), icon pass, accessibility sizes.

## 6. Rules (from crash history — normative)
- Every slice: trace → implement → CI build → gates (`PACKAGE/LABEL/
  WORDMARK/ICON/PROMO-GONE/STRINGS/ID-CONTRACT`) → APK-contents check →
  device test before next slice.
- Never delete ID'd views; never reorder adapter/tab children; never leave
  registers undefined; check twin-dex; keep prior release + commit intact.
- No runtime claims without screenshots/recordings. No engine/serialization
  changes. No mock controls.
