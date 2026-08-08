from pydantic import BaseModel


class MatchingRequest(BaseModel):
    resume_text: str
    job_description: str


class MatchingResponse(BaseModel):
    match_score: float
    matched_skills: list[str]
    missing_skills: list[str]