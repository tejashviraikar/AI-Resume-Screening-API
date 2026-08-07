import ast
import re
import pandas as pd

def clean_text(text: str) -> str:
    """
    Clean text by removing special characters,
    multiple spaces, and converting to lowercase.
    """

    if pd.isna(text):
        return ""

    text = text.lower()

    text = re.sub(r"\n", " ", text)

    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

def convert_skills_to_list(skill_string):
    """
    Convert the string representation of a list
    into a Python list.
    """

    if pd.isna(skill_string):
        return []

    try:
        skills = ast.literal_eval(skill_string)

        return [skill.strip().lower() for skill in skills]

    except Exception:
        return []

import re

def extract_job_skills(job_description, skill_list):
    """
    Extract skills from a job description
    using a predefined skill list.
    """

    text = clean_text(job_description)

    found = []

    for skill in skill_list:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(list(set(found)))

def normalize_skill(skill: str) -> str:
    """
    Normalize skill names.
    """

    skill = skill.lower().strip()

    replacements = {
        "node js": "node.js",
        "nodejs": "node.js",
        "js": "javascript",
        "ml": "machine learning",
        "ai": "artificial intelligence",
        "postgres": "postgresql",
        "c sharp": "c#"
    }

    return replacements.get(skill, skill)

normalized = []

for skill in unique_skills:
    normalized.append(normalize_skill(skill))

normalized = sorted(set(normalized))

print(len(normalized))

with open("../data/skills/master_skills.txt", "w", encoding="utf-8") as file:
    for skill in normalized:
        file.write(skill + "\n")