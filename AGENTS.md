# Agent Instructions — DeepMap

Read README.md, CONTRIBUTING.md, FEATURE_UPGRADE_PLAN.md and ACTIVITY_LOG.md first.

- Treat DeepMap as a coarse coordinate/terrain profiling prototype, not navigation or safety software.
- Validate finite latitude/longitude bounds, grid precision, identifiers and terrain labels.
- Preserve JSON compatibility or document schema changes.
- Add deterministic tests for equator, negative coordinates, dateline, poles and invalid inputs.
- Do not invent geospatial datasets or performance claims.
- Work on a branch and open a PR; do not merge or deploy autonomously.
