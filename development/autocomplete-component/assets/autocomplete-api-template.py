"""
Autocomplete API endpoint template
"""
from fastapi import APIRouter
from typing import List
import json
from pathlib import Path

router = APIRouter()

# Load data from JSON file (adjust path as needed)
DATA_FILE = Path(__file__).parent.parent / "data" / "{DATA_FILENAME}"


def load_data():
    """Load data from JSON file"""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Support both direct list and wrapped format
    if isinstance(data, dict) and '{DATA_KEY}' in data:
        return data['{DATA_KEY}']
    
    if isinstance(data, list):
        return data
    
    return []


@router.get("/{ENDPOINT_PATH}/search")
async def search_{ENDPOINT_NAME}(q: str = ""):
    """
    Search {RESOURCE_NAME}
    
    Parameters:
    - q: Search query
    
    Returns:
    - List of matching items (max {MAX_RESULTS})
    """
    items = load_data()
    
    if not q:
        # No query: return top items
        return items[:{MAX_RESULTS}]
    
    q = q.strip().lower()
    
    # Search logic: match against multiple fields
    matches = []
    for item in items:
        # Primary field exact match
        if item['{PRIMARY_FIELD}'].lower().startswith(q):
            matches.append({**item, "priority": 1})
        # Secondary field contains match
        elif q in item['{SECONDARY_FIELD}'].lower():
            matches.append({**item, "priority": 2})
        # Tertiary field match (if exists)
        elif '{TERTIARY_FIELD}' in item and q in item['{TERTIARY_FIELD}'].lower():
            matches.append({**item, "priority": 3})
    
    # Sort by priority
    matches.sort(key=lambda x: x['priority'])
    
    # Remove priority field
    results = [{k: v for k, v in m.items() if k != 'priority'} for m in matches]
    
    # Return top results
    return results[:{MAX_RESULTS}]


@router.get("/{ENDPOINT_PATH}/all")
async def get_all_{ENDPOINT_NAME}():
    """Get all {RESOURCE_NAME}"""
    return load_data()
