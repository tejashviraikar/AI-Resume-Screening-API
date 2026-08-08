from fastapi import APIRouter

from app.schemas.skill import (
    SkillExtractionRequest,
    SkillExtractionResponse
)

from app.services.skill_service import extract_skills_from_text

from app.schemas.matching import (
    MatchingRequest,
    MatchingResponse
)

from app.services.matching_service import match_resume_to_job 

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "API is running successfully"
    }


@router.post(
    "/extract-skills",
    response_model=SkillExtractionResponse
)
def extract_skills(request: SkillExtractionRequest):

    skills = extract_skills_from_text(request.text)

    return {
        "skills": skills
    }


@router.post(
    "/match",
    response_model=MatchingResponse
)
def match_resume(request: MatchingRequest):

    result = match_resume_to_job(
        request.resume_text,
        request.job_description
    )

    return result