from pathlib import Path

def load_skills(filepath):
    """
    Load skills from a text file.
    """

    with open(filepath, "r", encoding="utf-8") as file:
        skills = file.readlines()

    return [skill.strip().lower() for skill in skills]