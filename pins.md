# Toolchain pins (Beyond Effects canary)

All pins re-verified against local evidence on 2026-10-14 unless noted.

- Apktool 3.0.3 — release jar, sha256
  `dbf930b076c6b9be08d57c449cacefc3bdd6b71ebd59b3066fc0e1f5b14f9423`,
  15,478,013 bytes (re-hashed locally; REAL pin).
- JDK 17 (`actions/setup-java`, Temurin, `java-version: '17'`).
- Android build-tools 35.x primary, 34.x fallback CANDIDATE for `$`-name tolerance
  (candidate status per Phase 2M — decided by the fixture canary, not assumed).
- GitHub Actions tags below are tag pins; SHA-pinning is a hardening step at
  authoring time (SHAs UNVERIFIED here — never invented).
- No secrets are used by the canary workflow. Debug signing (if ever added) uses
  an in-run throwaway key, never a stored keystore.
