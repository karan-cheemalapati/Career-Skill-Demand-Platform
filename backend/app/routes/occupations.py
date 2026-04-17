from fastapi import APIRouter, HTTPException
from backend.app.data.loader import load_merged_data, load_occupations_data

router = APIRouter()


@router.get("/top-occupations")
def get_top_occupations():
    df = load_merged_data()

    top_occupations = (
        df[["soc_code", "title", "a_mean", "a_median", "tot_emp"]]
        .drop_duplicates()
        .sort_values("a_mean", ascending=False)
        .head(10)
    )

    results = [
        {
            "soc_code": row["soc_code"],
            "title": row["title"],
            "a_mean": None if str(row["a_mean"]) == "nan" else float(row["a_mean"]),
            "a_median": None if str(row["a_median"]) == "nan" else float(row["a_median"]),
            "tot_emp": None if str(row["tot_emp"]) == "nan" else float(row["tot_emp"]),
        }
        for _, row in top_occupations.iterrows()
    ]

    return {"top_occupations": results}


@router.get("/occupation/{occupation_id}")
def get_occupation_by_id(occupation_id: str):
    occupations_df = load_occupations_data()
    merged_df = load_merged_data()

    occupation_info = occupations_df[occupations_df["soc_code"].astype(str) == str(occupation_id)]

    if occupation_info.empty:
        raise HTTPException(status_code=404, detail="Occupation not found")

    occupation_row = occupation_info.iloc[0]

    occupation_merged = merged_df[merged_df["soc_code"].astype(str) == str(occupation_id)]

    top_skills = (
        occupation_merged[["element_name", "data_value"]]
        .drop_duplicates()
        .sort_values("data_value", ascending=False)
        .head(10)
    )

    skills = [
        {
            "skill_name": row["element_name"],
            "data_value": round(float(row["data_value"]), 2),
        }
        for _, row in top_skills.iterrows()
    ]

    salary_info = None
    if not occupation_merged.empty:
        salary_row = occupation_merged.iloc[0]
        salary_info = {
            "a_mean": None if str(salary_row["a_mean"]) == "nan" else float(salary_row["a_mean"]),
            "a_median": None if str(salary_row["a_median"]) == "nan" else float(salary_row["a_median"]),
            "tot_emp": None if str(salary_row["tot_emp"]) == "nan" else float(salary_row["tot_emp"]),
            "preferred_education": None if str(salary_row["preferred_education"]) == "nan" else salary_row["preferred_education"],
            "preferred_edu_pct": None if str(salary_row["preferred_edu_pct"]) == "nan" else float(salary_row["preferred_edu_pct"]),
        }

    return {
        "soc_code": occupation_row["soc_code"],
        "title": occupation_row["title"],
        "description": occupation_row["description"],
        "salary_and_education": salary_info,
        "top_skills": skills,
    }