# Changelog — QS Lab EBIFE Research Package

All notable changes to this package. The version in `VERSION` is the package version installed by the install prompt.

## 1.0.0 — 2026-07-16
Initial release.
- Added command `/qsl-spy-ben1` — creates the **SPY Buy and Hold Benchmark 1** strategy file.
- Added strategy **SPY-BEN1** (`strategies/SPY Buy and Hold Benchmark 1.md`) — 100% SPY buy-and-hold, $100,000, 2005–2026.
- Added the install prompt (`INSTALL.md`) — installs commands into `~/.claude/skills/` so they work in every Claude Code session.
- Package distributed as a hosted zip: `https://dev.quantstrategylab.com/qslab-kit.zip`.

## 1.0.1 — 2026-07-16
- Rewrote the install prompt so the request is legible: states who publishes the package and what is inside, and makes Claude show the version and command list **before** installing. Installing skills adds instructions to the student's Claude Code, so the inspection is a designed step, not something to suppress.
- Install now adds skills alongside existing ones and changes nothing else.

## 1.1.0 — 2026-07-17
- Strategy delivery redesigned as fixed two-file packages: `spy-ben1.py` (canonical code) + `spy-ben1.pdf` (description). No code is shown on course pages; Claude downloads the package byte-for-byte and verifies SHA-256 checksums against `manifest.json`. Claude never generates or retypes strategy code — every student gets the identical files.
- Replaced `strategies/SPY Buy and Hold Benchmark 1.md` with the `strategies/spy-ben1/` package.
- Student experience is plain language: copy-button prompts on the course page; no slash commands to learn. The install flow and `/qsl-spy-ben1` are deprecated (skill retained temporarily, to be removed).

## 1.1.1 — 2026-07-17
- Clipboard delivery: the get-strategy step now ends with Claude piping the verified code file directly onto the student's clipboard (pbcopy/clip — byte-exact, never retyped). The student pastes straight into QuantConnect; no file opening required. PDF instructions updated accordingly. (A copy button inside the PDF was evaluated and rejected: PDF JavaScript does not run in macOS Preview or browser viewers.)

## 1.2.0 — 2026-07-17
- Delivery model final: the strategy code never lands on the student's computer. The course page has a "Copy strategy code" button that fetches the canonical file live from this repository, verifies its SHA-256 against manifest.json in the browser, and puts it on the clipboard. No files, no downloads, no Claude in the code path. Claude's role is explanation and results analysis only.
- PDF description updated to teach the button flow; it is opened from the repository, not saved locally.

## 1.3.0 — 2026-07-17
- Naming convention adopted: type prefix first — BEN- for benchmarks, S- for single strategies, P- for portfolios of strategies ("portfolio" chosen over "ensemble": the academically standard term for capital allocated across independent strategies, and plain language for students). SPY-BEN1 renamed to BEN-SPY; package folder is now strategies/ben-spy/. Full citation format: BEN-SPY · v1.3.0 · sha <fingerprint>.

## 1.3.1 — 2026-07-17
Housekeeping release — the repository now documents the current architecture completely.
- README rewritten: the repository is a source of truth of fixed, checksummed strategy packages consumed by the QSL platform; delivery flow, catalog, layout, and integrity rules stated.
- Added PACKAGE-SPEC.md (package format, manifest schema, naming convention, release process, delivery contract), STRATEGIES.md (the catalog: live / planned / retired), and CLAUDE.md (rules for AI agents: the bytes are the product; every file change is a release).
- Removed the obsolete v1.0 delivery model: INSTALL.md, COMMANDS.md, and the deprecated /qsl-spy-ben1 skill. The hosted zip distribution is retired.

## 1.3.2 — 2026-07-17
- Added the MIT License. The free-course packages are open; the license maximizes trust and lets students use and adapt what they learn from.

## 1.4.0 — 2026-07-25
Repository renamed **qsl-mi → qsl-ebife** (Marco directive), matching the course acronym after the course rename to "Evidence-Based Investing for Everyone" (2026-07-24). GitHub redirects the old URLs, including raw URLs; consumers should move to the new base `https://raw.githubusercontent.com/mdiprima1/qsl-ebife/main/...`.
- Package brand updated in README, CHANGELOG, CLAUDE.md ("QS Lab MI Research Package" → "QS Lab EBIFE Research Package"); PACKAGE-SPEC delivery-contract URL updated.
- Strategy files untouched by design: `ben-spy.py` still carries the old brand in its header comment because changing any strategy byte changes its fingerprint. The comment will be updated in the next substantive BEN-SPY release.
