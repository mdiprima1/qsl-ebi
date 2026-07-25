# Instructions for AI agents working in this repository

You are in the **QS Lab EBIFE Research Package** — the canonical source of the strategy packages for the QSL course "Evidence-Based Investing for Everyone." Read `README.md` for the architecture and `PACKAGE-SPEC.md` for the package format before changing anything.

## The one rule that outranks everything

**The bytes are the product.** Students receive these files byte-for-byte, verified by SHA-256 against each package's `manifest.json`. Therefore:

- Never modify a strategy file (`.py` or `.pdf`) unless the task explicitly asks for it.
- Never "improve," reformat, lint, or annotate strategy code in passing.
- Any change to a package file is a **release** and must follow the release process in `PACKAGE-SPEC.md` — regenerate fingerprints, bump `VERSION`, add a `CHANGELOG.md` entry, update `STRATEGIES.md`, one commit.
- Fingerprints are computed (`shasum -a 256`), never typed or copied from memory.

## What things are

| Path | What it is |
|---|---|
| `strategies/<id>/` | One package: code + PDF description + manifest. Folder name = lowercase strategy ID. |
| `VERSION`, `CHANGELOG.md` | Repository release state. A push to `main` is a release — consumers fetch raw `main`. |
| `PACKAGE-SPEC.md` | The package format, manifest schema, naming convention, release process. |
| `STRATEGIES.md` | The catalog. Update it with every release. |

## Conventions

- Strategy IDs: `BEN-` benchmarks, `S-` single strategies, `P-` portfolios of strategies.
- Citation format: `BEN-SPY · v1.3.0 · sha acaec7d7…`.
- All prose (PDFs, docs) follows the QSL Language Character Model: simple sentences, plain words, no coined labels, no exclamation marks, never "retail trader."
- PDFs are generated with reportlab in the QSL house style (navy/gold/cream); regenerate rather than hand-edit.

## Adding a new package (the standard task)

1. Create `strategies/<id>/` with `<id>.py`, `<id>.pdf`, `manifest.json` per `PACKAGE-SPEC.md`.
2. The code must be the exact, approved canonical version — sourced from the QSL strategy vault or explicitly provided. Do not write strategy logic yourself.
3. Follow the release process; update `STRATEGIES.md` (move from Planned to Live).
4. The platform's My Strategies page consumes this repo by raw URL — coordinate its registry entry separately; nothing in this repo references the platform.

## Who consumes this repository

- The QSL platform "My Strategies" page (browser-side fetch + SHA-256 verification + clipboard copy).
- QSL Lab Reports and the strategy vault, which cite packages by ID · version · sha.

If a task seems to require breaking any rule above, stop and ask.
