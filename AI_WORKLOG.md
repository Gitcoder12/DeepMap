# AI Worklog

## Assessment
- Date: 2026-11-15
- Branch: `audit/initial-assessment-2026-11-15`
- Recommendation: Improve
- Maturity: Runnable local CLI prototype with coordinate-grid and terrain-friction helpers.

## Purpose and implemented scope
DeepMap is a local-first Python CLI for recording coordinates, classifying a small set of terrain types, calculating a rule-based friction score, and persisting mapped zones as JSON.

Verified implementation:
- `main.py` provides coordinate registration, coordinate lookup, and a CLI loop.
- `geo_engine.py` validates numeric, finite latitude/longitude and positive grid precision.
- `storage.py` loads and saves local JSON state.
- `locations.json` provides a small location dataset.
- `tests/test_geo_engine.py` covers grid hashing and several invalid coordinate cases.
- `.github/workflows/tests.yml` compiles Python and runs unittest discovery.

## Architecture and health
The current implementation is a small, single-process CLI with a rule-based geospatial helper and JSON persistence. The README architecture diagram references `app.py`, `api_client.py`, `pathfinder.py`, and `deep_map_data.json`; these paths were not present in the inspected root tree. Treat those README references and any associated feature claims as stale until reconciled with source.

## Findings
### P1 — Unhandled coordinate validation errors in the CLI
`geo_engine.generate_grid_hash` correctly raises `ValueError` for out-of-range or non-finite coordinates, but `main.py` calls it after only catching float-conversion errors. Numeric input such as latitude 91 can therefore terminate the CLI instead of returning a validation message. Add a focused CLI-level regression test and catch validation errors at the input boundary.

### P1 — Corrupt persistence silently falls back to defaults
`storage.load_map_data` returns default data after JSON decode or read errors. A subsequent save can overwrite the unreadable file, masking possible data loss. Preserve the corrupt file, surface a clear recovery warning, and require an explicit reset or recovery path.

### P2 — Persistence is not atomic
`save_map_data` writes directly to the destination file and only prints on `OSError`; callers cannot determine whether the save succeeded. Use a same-directory temporary file plus atomic replace, and return or raise a clear result.

### P2 — Terrain friction is a heuristic, not a validated hazard metric
The current formulas use simple integer divisions and terrain labels. They are not calibrated against measured navigation outcomes. Document the score as an illustrative heuristic and add tests for negative, extreme, and invalid metric inputs.

### P2 — Test coverage is narrow
The inspected test suite covers grid hashing only. Storage recovery, write failure, terrain friction, and CLI input flows are not covered.

## Checks and evidence
- Inspected the root tree, README, `main.py`, `geo_engine.py`, `storage.py`, `tests/test_geo_engine.py`, and CI workflow.
- CI workflow defines `python -m compileall -q .` and `python -m unittest discover -s tests -v`.
- Local test execution: NOT RUN in this environment.
- Current default-branch combined status query returned no status entries; this is not evidence of a passing or failing run.
- Independent model review: NOT PERFORMED.
- Links checked: repository paths and relative architecture references by source-tree comparison; external demo links not exhaustively checked.

## Next actions
1. Fix and test CLI handling of invalid numeric coordinates.
2. Make JSON persistence recoverable and atomic.
3. Validate terrain metric input and document heuristic limitations.
4. Align README architecture with files that actually exist.
5. Add storage and CLI regression tests; confirm CI on the PR head.
