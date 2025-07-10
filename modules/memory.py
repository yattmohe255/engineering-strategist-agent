import json
from datetime import datetime
import os

MEMORY_FILE = "logs/project_log.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {"projects": []}
    with open(MEMORY_FILE, 'r') as file:
        return json.load(file)

def save_memory(data):
    with open(MEMORY_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_project(name, description, technologies, stakeholders, lessons):
    memory = load_memory()
    new_entry = {
        "name": name,
        "description": description,
        "technologies": technologies,
        "stakeholders": stakeholders,
        "lessons": lessons,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    memory["projects"].append(new_entry)
    save_memory(memory)
