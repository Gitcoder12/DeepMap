# CleanMap Data Schema

## Location
| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique location ID (L001...) |
| name | string | Human-readable area name |
| lat / lng | float | GPS coordinates |
| cleanliness_score | int (0–100) | Aggregated cleanliness rating |
| last_updated | date | ISO date of last data update |
| resources | string[] | Available public resources at this location |
| reports | int | Number of user reports submitted |

## Resource Types
- `bin` — Public waste bin
- `recycling` — Recycling drop point
- `washroom` — Public toilet/washroom
- `water_point` — Public drinking water

## Cleanliness Score Bands
| Score | Label |
|-------|-------|
| 80–100 | Excellent |
| 60–79 | Good |
| 40–59 | Average |
| 0–39 | Poor |
