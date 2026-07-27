# QS Lab EBI Research Package

**Version 1.6.0** · The public delivery surface of the QSL course **Evidence-Based Investing for Everyone** (Quantitative Strategy Lab, quantstrategylab.com): the strategy packages and the client-facing tools students receive.

## Scope — what this repository is for (Marco, 2026-07-27)

**This repository holds only the client-facing tools and the strategies given to students.** It is a source of truth, not an app, and nothing else belongs here.

**Course content does not live here.** It lives in **`qsl-product/EBI Coursecontent/`**, which is private — so units, slides, narration, decks and drafts are not visible while they are being made. This repository is public, and everything pushed to it is visible immediately: correct for a strategy package a student is meant to fetch and verify, and wrong for a unit in progress.

| Zone | Status |
|---|---|
| **`strategies/`** | **The purpose of this repository.** Every strategy taught in the course, as a fixed, versioned, checksummed package delivered byte-for-byte — never generated, retyped, or altered between here and the student's clipboard. Governed by `PACKAGE-SPEC.md`. |
| **Client-facing research tools** | Belong here too, for the same reason: they are a thing the student receives and runs. Delivery mechanism not yet fixed. |
| **`modules/`, `workshop/`** | **Superseded as the content home** (2026-07-27). `modules/` was never populated; `workshop/` holds earlier material now treated as reference. **Do not add new course content here** — it goes to `qsl-product/EBI Coursecontent/`. |

## Canonical sources (live in qsl-hq — referenced here, never copied)

The course's defining documents live in the **qsl-hq** hub and are the single source of truth — do not copy them here, link to them:

- **Syllabus of record:** `qsl-hq/QSL_Syllabus/SYLLABUS.md` — *Evidence-Based Investing for Everyone*, 5 chapters / 27 units (overview: `qsl-hq/QSL_Syllabus/README.md`). This is the latest, signed syllabus.
- **The QSL Strategy Validation Process:** `qsl-hq/QSL VAL/` — start at `VALIDATION-SYSTEM-OVERVIEW.md` (four levels, thirteen tests) and `QSL VAL-Mission.md`.

When a module here *teaches* the syllabus or the validation process, it is a beginner-facing translation of these documents (per the QSL rule that public text translates the standard rather than copying its vocabulary) — the definitions stay canonical in qsl-hq.

## How delivery works

1. A student opens **My Strategies** in their QSL account.
2. The page fetches the strategy's code and `manifest.json` directly from this repository (raw URLs).
3. The browser recomputes the code file's SHA-256 and compares it to the manifest — **the fingerprint check**.
4. Only on a match does the **Copy code** button arm; one click puts the exact bytes on the clipboard, ready to paste into a Python algorithm on QuantConnect.

The code never appears on screen and never lands on the student's machine. Every student runs the identical strategy, so every result is comparable — the foundation of QSL's validation teaching.

## Strategy catalog

See **[STRATEGIES.md](STRATEGIES.md)** for the live catalog. Currently:

| ID | Name | Version | Status |
|---|---|---|---|
| `BEN-SPY` | SPY Buy and Hold Benchmark | 1.3.0 | Live |
| `BEN-6040` | 60/40 Benchmark | — | Planned (course Unit 5) |
| `S-DM1` | Dual Momentum V1 | — | Planned (course Unit 9) |

## Naming convention

Type prefix first: **`BEN-`** benchmarks · **`S-`** single strategies · **`P-`** portfolios of strategies.
Full citation of any strategy artifact: **`ID · v<version> · sha <fingerprint>`** — name, release, cryptographic proof. The fingerprint changes with every release by design; it identifies exact bytes.

## Repository layout

```
strategies/
  ben-spy/            one folder per package (lowercase form of the strategy ID)
    ben-spy.py        the canonical strategy code (QuantConnect, Python)
    ben-spy.pdf       the student-facing description
    manifest.json     id, name, version, SHA-256 fingerprints of both files
modules/              course-content library: ch1…ch5 chapter folders, one module per concept
workshop/             work-in-progress space; material promotes into modules/ when mature
VERSION               package version (semver)
CHANGELOG.md          every change, versioned
PACKAGE-SPEC.md       the package format and release process
STRATEGIES.md         the catalog
CLAUDE.md             instructions for AI agents working in this repository
```

## Integrity rules

- **The bytes are the product.** Any change to a strategy file — even one character — requires: regenerate fingerprints in `manifest.json`, bump `VERSION`, add a `CHANGELOG.md` entry, in one commit.
- **Fingerprints are never edited by hand**; they are computed from the files.
- Package folders are never reused for a different strategy; retired packages are removed, their IDs never reassigned.
- Certification records (QSL Lab Reports) pin to the fingerprint: a validation applies to exactly the bytes it tested.

## Consumers

- The QSL platform "My Strategies" page (fetches raw files + verifies fingerprints in the browser).
- QSL Lab Reports and the QSL strategy vault (cite packages by ID · version · sha).

---
© Quantitative Strategy Lab · [MIT License](LICENSE). Educational materials for the QSL course; not investment advice.
