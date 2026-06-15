"""Global Configurations and Terrain Matrix Constants for DeepMap v1.0."""

# Environmental Layers Matrix
TERRAIN_DESERT = "🏜️ Desert"
TERRAIN_OCEAN = "🌊 Ocean"
TERRAIN_MOUNTAIN = "🏔️ Mountain"

# Base Data Schema Fallback
DEFAULT_DATA = {
    "mapped_zones": {},    # Maps mathematical grid block hashes to topological profiles
    "saved_waypoints": []  # High-value contextual resource locations discovered in extreme environments
}

# Simple, dependency-free ANSI Colors
CLR_DEEP_BLUE = "\033[94m"   # Deep Marine Environments
CLR_SAND_GOLD = "\033[93m"   # Arid Sandy Deserts
CLR_ROCK_GRAY = "\033[90m"   # Vertical Elevations
CLR_EMERALD   = "\033[92m"   # Verified Profile Targets
CLR_RED       = "\033[91m"   # Structural Navigation Risks
CLR_RESET     = "\033[0m"
