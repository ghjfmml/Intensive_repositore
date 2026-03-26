import os 
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "database.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    
    with open (DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        return json.dump(data, file, ensure_ascii=False, indent=4)