# Package specification

**Spec version 1 · applies to package version 1.3.0 and later.**

A strategy package is one folder under `strategies/`, named with the lowercase form of the strategy ID (`BEN-SPY` → `ben-spy/`). It contains exactly three files.

## Files

| File | Purpose | Rules |
|---|---|---|
| `<id>.py` | The canonical strategy code | Pure Python for QuantConnect. Paste-ready: a student pastes it over the QC template unchanged. Header comment carries strategy ID and package version. No external dependencies beyond `AlgorithmImports`. |
| `<id>.pdf` | The student-facing description | What the strategy is, its specification table (including the Strategy ID), how to run it in QuantConnect, what to expect. Two pages maximum. Plain language per the QSL Language Character Model. |
| `manifest.json` | The integrity record | See schema below. Fingerprints are computed, never hand-edited. |

## manifest.json schema

```json
{
  "id": "ben-spy",                                  // lowercase folder id
  "strategy_id": "BEN-SPY",                         // canonical ID (BEN- / S- / P- convention)
  "name": "SPY Buy and Hold Benchmark",             // display name
  "vault_ref": "BEN-SPY (vault benchmarks table)",  // link into the QSL strategy vault
  "package_version": "1.3.0",                       // repo VERSION at release
  "files": {
    "ben-spy.py":  { "sha256": "<64 hex chars>" },
    "ben-spy.pdf": { "sha256": "<64 hex chars>" }
  }
}
```

## Naming convention

- **`BEN-`** benchmarks · **`S-`** single strategies · **`P-`** portfolios of strategies.
- IDs are short and stable: `BEN-SPY`, `BEN-6040`, `S-DM1`.
- Citation format everywhere (Lab Reports, vault, support): `BEN-SPY · v1.3.0 · sha acaec7d7…` (first 12 hex of the code file's SHA-256 is the display form; records store the full hash).

## Release process (every change to any package)

1. Edit the package files (or add a new package folder).
2. Regenerate the PDF if content changed.
3. Recompute both SHA-256 fingerprints; write them into `manifest.json`.
4. Bump `VERSION` (semver: new package or delivery-model change = minor; content fix = patch).
5. Add a `CHANGELOG.md` entry stating what changed and why.
6. One commit for the whole release; push to `main`. Consumers fetch `main` raw — a push is a release.

## Delivery contract (what consumers rely on)

- Raw URLs are stable: `https://raw.githubusercontent.com/mdiprima1/qsl-ebi/main/strategies/<id>/<file>`.
- The browser (or any consumer) MUST verify the code file's SHA-256 against the manifest before use; on mismatch, refuse delivery.
- The code file is delivered byte-for-byte. No consumer may reformat, annotate, or "improve" it.
