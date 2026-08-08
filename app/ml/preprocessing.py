import ast
import re
import pandas as pd


def clean_text(text: str) -> str:
    if pd.isna(text):
        return ""

    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def convert_skills_to_list(skill_string):
    if pd.isna(skill_string):
        return []

    try:
        skills = ast.literal_eval(skill_string)
        return [skill.strip().lower() for skill in skills]
    except Exception:
        return []


def extract_job_skills(job_description, skill_list):
    text = clean_text(job_description)

    found = []

    for skill in skill_list:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(set(found))