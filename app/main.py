from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Resume Screening API",
    description="AI-powered Resume Screening and Job Matching API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Resume Screening API"
    }