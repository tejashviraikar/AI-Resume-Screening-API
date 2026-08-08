from pathlib import Path

from app.ml.preprocessing import extract_job_skills


BASE_DIR = Path(__file__).resolve().parents[2]

SKILLS_FILE = BASE_DIR / "data" / "skills" / "master_skills.txt"


def load_master_skills():
    with open(SKILLS_FILE, "r", encoding="utf-8") as file:
        return [
            line.strip().lower()
            for line in file
            if line.strip()
        ]


def extract_skills_from_text(text: str):
    skills = load_master_skills()

    return extract_job_skills(
        text,
        skills
    )