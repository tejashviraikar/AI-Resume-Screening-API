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