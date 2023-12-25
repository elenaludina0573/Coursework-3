import json
from config import DATA_DIR

def get_all_operations(path):
    with open(path) as file:
        content = json.load(file)
        return content





