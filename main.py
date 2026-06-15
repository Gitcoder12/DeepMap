import sys
from config import (
    CLR_DEEP_BLUE, 
    CLR_SAND_GOLD, 
    CLR_ROCK_GRAY, 
    CLR_EMERALD, 
    CLR_RED,
    CLR_RESET, 
    TERRAIN_DESERT, 
    TERRAIN_OCEAN, 
    TERRAIN_MOUNTAIN
)
from storage import load_map_data, save_map_data
from geo_engine import generate_grid_hash, calculate_terrain_friction

def register_deep_zone(data):
    print(f"\n{CLR_DEEP_BLUE}🌐 Deep Coordinate Mapping Initialized{CLR_RESET}")
    try:
        lat = float(input("Enter Latitude (e.g., 23.4162 for Sahara): ").strip())
        lon = float(input("Enter Longitude (e.g., 25.6628): ").strip())
    except ValueError:
        print(f"{CLR_RED}⚠️ Coordinates must be numeric decimal floats.{CLR_RESET}")
        return

    print("\nSelect Primary Deep Terrain Profile Layer:")
    print(f"  {TERRAIN_OCEAN} (Ocean Trench Profiles)")
    print(f"  {TERRAIN_DESERT} (Arid Dune Formations)")
    print(f"  {TERRAIN_MOUNTAIN} (Vertical Continental Peaks)")
    
    choice = input("Select Layer (1-3): ").strip()
    if choice == "1":
        t_type = TERRAIN_OCEAN
        lbl_v = "Enter Depth metric in meters below sea level (e.g., -4500): "
    elif choice == "2":
        t_type = TERRAIN_DESERT
        lbl_v = "Enter Aridity/Heat Index hazard score (1-100): "
    elif choice == "3":
        t_type = TERRAIN_MOUNTAIN
        lbl_v = "Enter Peak Elevation metric in meters above sea level (e.g., 6200): "
    else:
        print(f"{CLR_RED}⚠️ Invalid terrain profiling layer assignment.{CLR_RESET}")
        return

    try:
        val = int(input(lbl_v).strip())
    except ValueError:
        print(f"{CLR_RED}⚠️ Value must be a valid integer parameter.{CLR_RESET}")
        return

    grid_id = generate_grid_hash(lat, lon)
    friction = calculate_terrain_friction(val, t_type)
    
    data["mapped_zones"][grid_id] = {
        "latitude": lat,
        "longitude": lon,
        "terrain": t_type,
        "vertical_metric": val,
        "navigation_friction": friction
    }
    
    save_map_data(data)
    print(f"\n✅ {CLR_EMERALD}Zone Locked! Spatial Grid ID '{grid_id}' mapped into local history matrix with a hazard rating of {friction}/100.{CLR_RESET}")

def scan_coordinates(data):
    print(f"\n{CLR_SAND_GOLD}📡 Deep Sub-surface Coordinate Scan{CLR_RESET}")
    try:
        lat = float(input("Enter Target Latitude: ").strip())
        lon = float(input("Enter Target Longitude: ").strip())
    except ValueError:
        print(f"{CLR_RED}⚠️ Coordinates must be numeric decimal floats.{CLR_RESET}")
        return
        
    grid_id = generate_grid_hash(lat, lon)
    zone = data["mapped_zones"].get(grid_id)
    
    if not zone:
        print(f"\n🛰️ {CLR_RED}Coordinates fall into uncharted space. Grid ID: {grid_id}{CLR_RESET}")
    else:
        print(f"\n🔍 {CLR_EMERALD}TERRAIN GRID PROFILE LOCATED:{CLR_RESET}")
        print(f"  📍 Spatial Block ID : {CLR_SAND_GOLD}{grid_id}{CLR_RESET}")
        print(f"  🗺️ Environmental Layer : {zone['terrain']}")
        print(f"  📐 Vertical Metric    : {zone['vertical_metric']} meters/units")
        print(f"  ⚠️ Navigation Hazard  : {CLR_RED}Friction Rating {zone['navigation_friction']}/100{CLR_RESET}")

def main():
    data = load_map_data()
    
    while True:
        print(f"\n{CLR_DEEP_BLUE}=================================================={CLR_RESET}")
        print(f"         {CLR_SAND_GOLD}DEEPMAP v1.0: THE SUB-SURFACE GEOMATRIX{CLR_RESET}   ")
        print(f"{CLR_DEEP_BLUE}=================================================={CLR_RESET}")
        print(" [1] Map an Uncharted Deep Zone Coordinate Block")
        print(" [2] Scan Target Coordinate Lat/Lon Metadata Profile")
        print(" [3] Exit Exploration Core")
        
        choice = input("\nSelect navigation parameter: ").strip()
        if choice == "1":
            register_deep_zone(data)
        elif choice == "2":
            scan_coordinates(data)
        elif choice == "3":
            print(f"\n{CLR_DEEP_BLUE}Exiting DeepMap mapping interface telemetry stream.{CLR_RESET}")
            break
        else:
            print(f"{CLR_RED}⚠️ Invalid choice selection parameters.{CLR_RESET}")

if __name__ == "__main__":
    main()
