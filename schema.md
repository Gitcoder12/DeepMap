# DeepMap Data Schema

This document describes the two data formats currently present in the repository. They serve different purposes and are not interchangeable.

## Runtime map file: `deep_map_data.json`

The CLI creates this file in the current working directory when a zone is saved. If it does not exist, `storage.py` starts from the following structure:

```json
{
  "mapped_zones": {},
  "saved_waypoints": []
}
```

### `mapped_zones`

An object keyed by a grid identifier generated from latitude and longitude, for example `"17.0_78.0"`. Each value contains:

| Field | Type | Meaning |
|---|---|---|
| `latitude` | number | Latitude in decimal degrees, from -90 to 90 |
| `longitude` | number | Longitude in decimal degrees, from -180 to 180 |
| `terrain` | string | One of the configured terrain labels: Ocean, Desert, or Mountain |
| `vertical_metric` | integer | User-supplied terrain metric; interpretation depends on terrain type |
| `navigation_friction` | number | Prototype heuristic returned by `calculate_terrain_friction` |

Grid precision defaults to one degree. This is a coarse grouping mechanism, not a navigation-grade spatial index.

### `saved_waypoints`

An array reserved by the current default data structure. The CLI does not yet read or write waypoint records.

## Bundled reference file: `locations.json`

This is a legacy sample dataset and is not loaded by the current terminal workflow. Its top-level fields are:

| Field | Type | Meaning |
|---|---|---|
| `version` | string | Dataset format version |
| `city` | string | Dataset's example city |
| `locations` | array | Sample location records |
| `resource_types` | string array | Supported resource labels in the legacy dataset |
| `score_bands` | object | Illustrative cleanliness-score ranges |

Each legacy location includes `id`, `name`, `lat`, `lng`, `cleanliness_score`, `last_updated`, `resources`, and `reports`.

## Limitations

All terrain-friction values and bundled location records are illustrative. DeepMap does not obtain live elevation, bathymetry, weather, hazard, or route data and must not be used as a navigation or safety system.
