from pydantic import BaseModel
from typing import List, Optional


class OccupationResult(BaseModel):
    soc_code: str
    title: str
    skill_score: Optional[float] = None
    average_skill_score: Optional[float] = None
    a_mean: Optional[float] = None
    a_median: Optional[float] = None
    tot_emp: Optional[float] = None
    preferred_education: Optional[str] = None


class TopSkillItem(BaseModel):
    skill_name: str
    skill_score: float


class FilterParams(BaseModel):
    skill: Optional[str] = None
    min_salary: Optional[float] = None
    min_skill_score: Optional[float] = None
    education: Optional[str] = None


class TextInsightResponse(BaseModel):
    input_text: str
    detected_skills: List[str] = []
    recommended_skills_to_add: List[str] = []
    top_occupations: List[OccupationResult] = []
    message: str


class GuidedQuestionsResponse(BaseModel):
    questions: List[str]


class FilterMetadataResponse(BaseModel):
    skills: List[str]
    education_levels: List[str]


class OccupationDetailResponse(BaseModel):
    found: bool
    soc_code: str
    title: Optional[str] = None
    description: Optional[str] = None
    a_mean: Optional[float] = None
    a_median: Optional[float] = None
    tot_emp: Optional[float] = None
    preferred_education: Optional[str] = None
    preferred_edu_pct: Optional[float] = None
    top_skills: List[TopSkillItem] = []
    message: Optional[str] = None


class InsightsSummaryResponse(BaseModel):
    questions: List[str]
    skills: List[str]
    education_levels: List[str]
    top_occupations: List[OccupationResult] = []


class OccupationFilterResponse(BaseModel):
    filters: FilterParams
    results: List[OccupationResult] = []