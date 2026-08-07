def skill_match(resume_skills, job_skills):
    """
    Compare resume skills with job skills.
    Returns match score, matched skills and missing skills.
    """

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched = sorted(list(resume_set.intersection(job_set)))
    missing = sorted(list(job_set - resume_set))

    if len(job_set) == 0:
        score = 0
    else:
        score = round((len(matched) / len(job_set)) * 100, 2)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }