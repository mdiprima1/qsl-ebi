# QS Lab EBIFE Research Package

**Version 1.3.2** · The canonical strategy packages for the QSL course **Evidence-Based Investing for Everyone** (Quantitative Strategy Lab, quantstrategylab.com).

This repository is a **source of truth, not an app**. Every strategy taught in the course lives here as a fixed, versioned, checksummed package. The course platform delivers these packages to students byte-for-byte — the code is never generated, retyped, or altered anywhere between this repository and the student's clipboard.

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
