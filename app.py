import os
import json

DATA_DIR = "data"
KARVANDS_PATH = os.path.join(DATA_DIR, "karvands.json")
# REPORT_PATH = os.path.join(DATA_DIR, "report.json")
line = "-" * 25

bootcamp_dict = {"title": "karvand Python", "year": "2026"}
karvands_list = []
karvand_manager = {"bootcamp": bootcamp_dict, "karvands": karvands_list}


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


def generate_id(karvands_list):
    if karvands_list == []:
        return 1

    else:
        counter = max(karvand["id"] for karvand in karvands_list)
        return counter + 1


def get_skills():
    print("## SKILLS: ##")
    skills_list = []
    adding_skills = True
    while adding_skills:
        name = input("Enter skill name: ").strip()
        if name == "":
            print("Skill name cannot be empty")
            continue
        while True:
            level = input("Enter skill level: ").strip()
            if level == "":
                print("Skill level cannot be empty")
                continue
            else:
                break
        score = get_valid_skill_score()
        skills_dict = {"name": name, "level": level, "score": score}
        skills_list.append(skills_dict)
        while True:
            user_response = (
                input("Do you want to add another skill? (yes or no) ").strip().lower()
            )
            if user_response not in ["yes", "no", "y", "n"]:
                print("Wrong command!")
                continue
            else:
                break
        if user_response in ["no", "n"]:
            adding_skills = False
    return skills_list


def get_valid_skill_score():
    while True:
        try:
            score = int(input("Enter skill score (0-100): ").strip())
            if score > 100 or score < 0:
                print("Score must be between 0 and 100")
            else:
                return score
        except ValueError:
            print("Invalid input! Please enter an integer number")


def get_education():
    print("## EDUCATION: ##")
    while True:
        degree = input("Enter karvand degree: ").strip()
        if degree == "":
            print("Degree cannot be empty")
            continue
        while True:
            field = input("Enter karvand field: ").strip()
            if field == "":
                print("Field cannot be empty")
                continue
            else:
                break
        education = {"degree": degree, "field": field}
        return education


def get_email():
    while True:
        email = input("Enter karvand email (example: ali@gmail.com):  ").strip()
        if "@" in email and "." in email:
            return email
        else:
            print("Email must contain '@' and '.' ")


def get_full_name(karvands_list):
    while True:
        full_name = input("Enter karvand full name (example: Ali Ahmadi): ").strip()
        if full_name == "":
            print("Full name cannot be empty")
            continue
        for karvand in karvands_list:
            if full_name.lower() == karvand["full_name"].lower():
                print("Duplicate karvand!")
                break
        else:
            return full_name


def get_city():
    while True:
        city = input("Enter karvand city: ").strip()
        if city == "":
            print("City cannot be empty")
            continue
        return city


def add_karvand(karvands_list):
    full_name = get_full_name(karvands_list)
    karvand_id = generate_id(karvands_list)
    email = get_email()
    city = get_city()
    education = get_education()
    skills = get_skills()
    karvand_dict = {
        "id": karvand_id,
        "full_name": full_name,
        "email": email,
        "city": city,
        "education": education,
        "skills": skills,
    }
    karvands_list.append(karvand_dict)
    return karvands_list


def show_all_karvands():
    karvand_manager = read_file()
    karvands = karvand_manager["karvands"]
    karvand_counter = 0
    if karvands:
        for karvand in karvands:
            karvand_counter += 1
            print(
                f"{line}\nKarvand information '{karvand_counter}'\n{line}\n"
                f"karvand id: {karvand['id']}\n"
                f"full name: {karvand['full_name']}\n"
                f"email: {karvand['email']}\n"
                f"city: {karvand['city']}\n"
                f"education degree: {karvand['education']['degree']}\n"
                f"education field: {karvand['education']['field']}"
            )
            skill_counter = 0
            for skill in karvand["skills"]:
                skill_counter += 1
                print(
                    f"{line}\nSKILL {skill_counter}\nskill name: {skill['name']}\nskill level: {skill['level']}\nskill score: {skill['score']}\n"
                )
    else:
        print("Karvand has not been added!")


def search_karvand_by_id():
    while True:
        try:
            input_karvand_id = input("Enter karvand id: ").strip()
            if input_karvand_id == "":
                print("Karvand id cannot be empty")
                continue
            input_karvand_id = int(input_karvand_id)
            break
        except ValueError:
            print("Invalid input! Please enter an integer number")

    karvand_manager = read_file()
    karvands = karvand_manager["karvands"]
    for karvand in karvands:
        if karvand["id"] == input_karvand_id:
            print(
                f"{line}\nKarvand information\n{line}\n"
                f"karvand id: {karvand['id']}\n"
                f"full name: {karvand['full_name']}\n"
                f"email: {karvand['email']}\n"
                f"city: {karvand['city']}\n"
                f"education degree: {karvand['education']['degree']}\n"
                f"education field: {karvand['education']['field']}"
            )
            skill_counter = 0
            for skill in karvand["skills"]:
                skill_counter += 1
                print(
                    f"{line}\nSKILL {skill_counter}\nskill name: {skill['name']}\nskill level: {skill['level']}\nskill score: {skill['score']}\n"
                )
            break
    else:
        print("No karvand with this id was found")


def search_karvand_by_skill():
    while True:
        input_skill = input("Enter skill: ").strip()
        if input_skill == "":
            print("skill cannot be empty")
            continue
        break

    found_karvand = False
    karvand_manager = read_file()
    karvands = karvand_manager["karvands"]

    for karvand in karvands:
        for skill in karvand["skills"]:
            if input_skill.lower() == skill["name"].lower():
                print(
                    f"karvand id: {karvand['id']} --> "
                    f"full name: {karvand['full_name']}\n"
                )
                found_karvand = True

    if not found_karvand:
        print("No karvand with this skill was found")


karvand_manager = read_file()
karvands_list = karvand_manager["karvands"]

running = True

while running:

    msg = input("""
1- Add karvand
2- Show all karvands
3- Search karvand by id
4- Search karvand by skill
5- Edit info karvand
6- Delete karvand
7- Report
8- Exit
---------------------------\n""").lower().strip()

    if msg in ["1", "add", "a", "add karvand", "1- add karvand"]:
        karvands_list = add_karvand(karvands_list)
        karvand_manager["karvands"] = karvands_list
        save_file(karvand_manager)
        print("Karvand added successfully")
    elif msg in [
        "2",
        "sh",
        "show",
        "2- show",
        "2- show all",
        "2- show all karvands",
        "show all karvands",
    ]:
        show_all_karvands()

    elif msg in [
        "3",
        "search by karvand id",
        "3- search karvand by id",
        "search by id",
        "3- search by id",
    ]:
        search_karvand_by_id()
    elif msg in [
        "4",
        "search karvand by skill",
        "4- search karvand by skill",
        "search by skill",
        "4- search by skill",
    ]:
        search_karvand_by_skill()
    elif msg == "5":
        print("Coming soon...")
    elif msg == "6":
        print("Coming soon...")
    elif msg == "7":
        print("Coming soon...")
    elif msg in ["8", "e", "exit", "8- exit"]:
        print("Program closed. Goodbye!")
        running = False
    else:
        print("Invalid choice!")
