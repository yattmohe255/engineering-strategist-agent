import json
from datetime import datetime

MEMORY_FILE = "project_memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"projects": []}

def add_project(name, description, technologies, stakeholders, lessons):
    memory = load_memory()
    memory["projects"].append({
        "name": name,
        "description": description,
        "technologies": technologies,
        "stakeholders": stakeholders,
        "lessons": lessons,
        "date_added": datetime.now().strftime("%Y-%m-%d")
    })
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)
