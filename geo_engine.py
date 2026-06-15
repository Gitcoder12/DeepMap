"""Spatial Grid Multi-Layer Hashing Engine for DeepMap v1.0."""
import math

def generate_grid_hash(lat, lon, precision=1.0):
    """
    Snaps raw floating-point latitude and longitude variables into a structural 
    coordinate grid block code (e.g., Lat 23.4162, Lon 25.6628 becomes '23.0_25.0').
    """
    grid_lat = math.floor(lat / precision) * precision
    grid_lon = math.floor(lon / precision) * precision
    return f"{grid_lat:.1f}_{grid_lon:.1f}"

def calculate_terrain_friction(vertical_value, terrain_type):
    """
    Calculates operational difficulty multipliers based on topological characteristics.
    Vast desert aridity, high mountain scaling, or abyssal marine pressure generate hazards.
    """
    base_friction = 10
    
    if terrain_type == "🌊 Ocean":
        # Deep marine trenches generate profound atmospheric and navigational strain
        return base_friction + abs(min(0, vertical_value)) // 100
    elif terrain_type == "🏔️ Mountain":
        # Intense vertical scaling introduces operational gravity hazards
        return base_friction + max(0, vertical_value) // 50
    elif terrain_type == "🏜️ Desert":
        # High hyper-aridity indexing adds logistics friction multipliers
        return base_friction + max(0, vertical_value) // 10
        
    return base_friction
