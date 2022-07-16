import json

def get_catalogue():
    with open("Catalogue.json", "r") as f:
        catalogue = json.load(f)
    return catalogue["catalogue"]

def get_featured():
    with open("Featured.json", "r") as f:
        featured = json.load(f)
    return featured["featured_entries"]

def get_entry(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data