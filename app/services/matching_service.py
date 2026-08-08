from app.ml.matching import skill_match
from app.ml.preprocessing import extract_job_skills
from app.services.skill_service import load_master_skills


def match_resume_to_job(
    resume_text: str,
    job_description: str
):
    # Load master skills
    skill_list = load_master_skills()

    # Extract skills from resume
    resume_skills = extract_job_skills(
        resume_text,
        skill_list
    )

    # Extract skills from job description
    job_skills = extract_job_skills(
        job_description,
        skill_list
    )

    # Compare skills
    result = skill_match(
        resume_skills,
        job_skills
    )

    return result