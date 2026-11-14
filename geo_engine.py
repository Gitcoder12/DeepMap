"""Coordinate grid and terrain-friction helpers for DeepMap."""

import math


def generate_grid_hash(lat, lon, precision=1.0):
    """Map valid latitude/longitude values to a coarse grid-cell identifier.

    Coordinates are validated before quantization so invalid GPS values and a
    zero/negative grid precision cannot silently produce misleading cells.
    """
    try:
        lat = float(lat)
        lon = float(lon)
        precision = float(precision)
    except (TypeError, ValueError) as exc:
        raise ValueError("Coordinates and precision must be numeric values.") from exc

    if not all(math.isfinite(value) for value in (lat, lon, precision)):
        raise ValueError("Coordinates and precision must be finite numbers.")
    if not -90 <= lat <= 90:
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    if not -180 <= lon <= 180:
        raise ValueError("Longitude must be between -180 and 180 degrees.")
    if precision <= 0:
        raise ValueError("Grid precision must be greater than zero.")

    grid_lat = math.floor(lat / precision) * precision
    grid_lon = math.floor(lon / precision) * precision
    return f"{grid_lat:.1f}_{grid_lon:.1f}"


def calculate_terrain_friction(vertical_value, terrain_type):
    """Return the prototype's rule-based terrain-friction estimate."""
    base_friction = 10

    if terrain_type == "🌊 Ocean":
        return base_friction + abs(min(0, vertical_value)) // 100
    if terrain_type == "🏔️ Mountain":
        return base_friction + max(0, vertical_value) // 50
    if terrain_type == "🏜️ Desert":
        return base_friction + max(0, vertical_value) // 10

    return base_friction
