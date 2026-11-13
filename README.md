# DeepMap

**A lightweight coordinate and terrain-profiling tool for exploration records.**

[![License](https://img.shields.io/badge/license-see%20LICENSE-lightgrey)](LICENSE)

DeepMap is a terminal-based prototype that maps latitude/longitude coordinates into coarse grid cells, stores terrain metadata, and calculates a simple terrain-friction score for each mapped zone.

## Features

- Convert decimal coordinates into one-degree grid identifiers.
- Register an ocean, desert, or mountain terrain profile for a grid cell.
- Calculate a rule-based friction score from the supplied terrain metric.
- Save and reload mapped zones through local JSON storage.
- Scan coordinates to retrieve a previously stored profile.

## Tech Stack

Python · JSON · Standard Library

## Quick Start

```bash
git clone https://github.com/Gitcoder12/DeepMap.git
cd DeepMap
python main.py
```

No third-party Python packages are required by the current implementation.

## How It Works

1. Enter latitude and longitude.
2. Select a terrain category and provide its depth, elevation, or aridity metric.
3. DeepMap assigns a grid ID and calculates a heuristic friction value.
4. The record is saved to `deep_map_data.json` in the working directory and can be retrieved by scanning coordinates in the same grid cell.

## Project Structure

```text
DeepMap/
├── main.py       # Interactive terminal workflow
├── geo_engine.py # Coordinate grid and friction calculations
├── storage.py    # Local JSON persistence
├── config.py     # Terrain labels, defaults, and terminal styling
├── locations.json # Bundled reference data (not read by the current CLI)
└── deep_map_data.json # Created at runtime after saving a mapped zone
```

## Scope and Limitations

DeepMap currently uses a coarse coordinate grid and hand-written terrain rules. It does not fetch live elevation, bathymetry, weather, hazard, or route data. Friction values are illustrative heuristics, not measured safety ratings or navigation advice.

## License

See [LICENSE](LICENSE).

---

## Project handbook

- [Activity log](ACTIVITY_LOG.md) — verified changes, checks and decisions.
- [Feature upgrade plan](FEATURE_UPGRADE_PLAN.md) — prioritised, testable work packages.
- [Company and team fit](COMPANY_FIT.md) — prospective employer fit, not customer claims.
- [README explanation draft](README_ADDENDUM_DRAFT.md) — beginner explanation plus technical scope.
- [README quality checklist](README_QUALITY_CHECKLIST.md) — clarity and evidence review.
- [Contributing](CONTRIBUTING.md) — contribution workflow.

- [Agent instructions](AGENTS.md)
- [Agent skills](SKILLS.md)
- [Contributing](CONTRIBUTING.md)

## Understanding the project

### In plain language

A terminal tool that groups latitude/longitude coordinates into coarse map cells and stores simple terrain profiles.

### Technical and research view

Python CLI and JSON persistence. Decimal latitude/longitude values are mapped into one-degree grid identifiers; terrain metadata is associated with cells and a rule-based friction score is calculated. This is a coarse exploration prototype, not a navigation or safety system.

The original feature list, setup instructions and limitations above remain authoritative. For future work, see [FEATURE_UPGRADE_PLAN.md](FEATURE_UPGRADE_PLAN.md), [ACTIVITY_LOG.md](ACTIVITY_LOG.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
