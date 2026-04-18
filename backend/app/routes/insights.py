from fastapi import APIRouter, Query
from pydantic import BaseModel, field_validator
from typing import Literal
from backend.app.data.loader import load_merged_data, clear_data_cache
from backend.app.data.insight_engine import analyze_input_text
from backend.app.data.filter_engine import filter_occupations_data
from backend.app.data.occupation_engine import get_occupation_detail_data
from backend.app.data.metadata_engine import get_filter_metadata_data
from backend.app.data.questions_engine import get_guided_questions_data
from backend.app.data.summary_engine import get_insights_summary_data
from backend.app.data.schemas import (
    TextInsightResponse,
    GuidedQuestionsResponse,
    FilterMetadataResponse,
    OccupationDetailResponse,
    InsightsSummaryResponse,
    OccupationFilterResponse,
)


router = APIRouter()


class TextInput(BaseModel):
    text: str
    mode: Literal["full", "occupations", "skills_gap", "learning"] = "full"

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Text input cannot be empty")
        return value.strip()


@router.post("/insights/text", response_model=TextInsightResponse)
def analyze_text(input_data: TextInput):
    df = load_merged_data()

    analysis = analyze_input_text(df, input_data.text)

    detected_skills = analysis["detected_skills"]
    recommended_skills = analysis["recommended_skills"]
    top_occupations = analysis["top_occupations"]
    
    response_detected_skills = detected_skills
    response_recommended_skills = recommended_skills
    response_top_occupations = top_occupations

    if input_data.mode == "occupations":
        response_recommended_skills = []

    elif input_data.mode == "skills_gap":
        response_top_occupations = []

    elif input_data.mode == "learning":
        response_detected_skills = []
        response_top_occupations = []

    return {
        "input_text": input_data.text,
        "detected_skills": response_detected_skills,
        "recommended_skills_to_add": response_recommended_skills,
        "top_occupations": response_top_occupations,
        "message": f"Text insight generated successfully in {input_data.mode} mode"
    }


@router.get("/insights/questions", response_model=GuidedQuestionsResponse)
def get_guided_questions():
    return get_guided_questions_data()


@router.get("/insights/occupations/filter", response_model=OccupationFilterResponse)
def filter_occupations(
    skill: str = Query(default=None),
    min_salary: float = Query(default=None),
    min_skill_score: float = Query(default=None),
    education: str = Query(default=None)
):
    df = load_merged_data()

    results = filter_occupations_data(
        df=df,
        skill=skill,
        min_salary=min_salary,
        min_skill_score=min_skill_score,
        education=education
    )

    return {
        "filters": {
            "skill": skill,
            "min_salary": min_salary,
            "min_skill_score": min_skill_score,
            "education": education
        },
        "results": results
    }


@router.get("/insights/filters/metadata", response_model=FilterMetadataResponse)
def get_filter_metadata():
    df = load_merged_data()
    return get_filter_metadata_data(df)

@router.get("/insights/occupation/{soc_code}", response_model=OccupationDetailResponse)
def get_insight_occupation_detail(soc_code: str):
    df = load_merged_data()
    return get_occupation_detail_data(df, soc_code)

@router.get("/insights/health")
def insights_health():
    return {
        "status": "ok",
        "service": "insights",
        "message": "Insights routes are working"
    }
    
@router.get("/insights/summary")
def get_insights_summary():
    df = load_merged_data()
    return get_insights_summary_data(df)

@router.post("/insights/cache/refresh")
def refresh_insights_cache():
    clear_data_cache()
    return {
        "status": "ok",
        "message": "Insights data cache cleared successfully"
    }