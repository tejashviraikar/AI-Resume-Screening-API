from fastapi import APIRouter

from app.schemas.skill import (
    SkillExtractionRequest,
    SkillExtractionResponse
)

from app.services.skill_service import extract_skills_from_text


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