import os
import json

DATA_DIR = "data"
KARVANDS_PATH = os.path.join(DATA_DIR, "karvands.json")

bootcamp_dict = {"title": "karvand Python", "year": "2026"}
karvand_manager = {"bootcamp": bootcamp_dict, "karvands": []}


def exist_data_file():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(KARVANDS_PATH):
        with open(KARVANDS_PATH, "w", encoding="utf-8") as file:
            json.dump(karvand_manager, file, indent=4, ensure_ascii=False)


def save_file(karvand_manager):
    with open(KARVANDS_PATH, "w", encoding="utf-8") as file:
        json.dump(karvand_manager, file, indent=4, ensure_ascii=False)


def read_file():
    exist_data_file()
    try:
        with open(KARVANDS_PATH, "r", encoding="utf-8") as file:
            karvand_manager = json.load(file)
    except json.JSONDecodeError:
        karvand_manager = {"bootcamp": bootcamp_dict, "karvands": []}
        save_file(karvand_manager)
        print("JSON file was empty or corrupted. A new file was created")
    return karvand_manager


karvand_manager = read_file()
print("Initial JSON storage is ready.")