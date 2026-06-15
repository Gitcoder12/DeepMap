import json
import os
from config import DEFAULT_DATA

MAP_FILE = "deep_map_data.json"

def load_map_data():
    """Reads structural spatial datasets from local storage safely."""
    if not os.path.exists(MAP_FILE):
        return json.loads(json.dumps(DEFAULT_DATA))
    try:
        with open(MAP_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return json.loads(json.dumps(DEFAULT_DATA))
        
    data.setdefault("mapped_zones", {})
    data.setdefault("saved_waypoints", [])
    return data

def save_map_data(data):
    """Persists updated terrain coordinates out to disk layout."""
    try:
        with open(MAP_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError as e:
        print(f"\n⚠️ Map state persistence failure: {e}")
