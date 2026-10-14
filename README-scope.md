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
- `.github/workflows/canary.yml` — toolchain canary (manual trigger, no secrets,
  no APK build).
- `.github/workflows/rebuild.yml` — APK reconstruction (manual trigger; original
  APK supplied at run time via URL+SHA, never committed; in-run throwaway test
  key only).
- `pins.md`, `.gitignore`, this note.

It does NOT contain: the original APK, decompiled sources, DEX, native
libraries, shipped assets, signing keys, backups, logs, or intermediates.
Reconstruction work stays disabled until separately approved.
