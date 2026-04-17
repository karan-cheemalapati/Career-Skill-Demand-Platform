from fastapi import APIRouter, HTTPException
from backend.app.data.loader import load_merged_data

router = APIRouter()


@router.get("/top-skills")
def get_top_skills():
    df = load_merged_data()

    top_skills = (
        df.groupby("element_name", as_index=False)["data_value"]
        .mean()
        .sort_values("data_value", ascending=False)
        .head(10)
    )

    results = [
        {
            "name": row["element_name"],
            "average_data_value": round(float(row["data_value"]), 2),
        }
        for _, row in top_skills.iterrows()
    ]

    return {"top_skills": results}


@router.get("/skill/{name}")
def get_skill_by_name(name: str):
    df = load_merged_data()

    skill_df = df[df["element_name"].str.lower() == name.lower()]

    if skill_df.empty:
        raise HTTPException(status_code=404, detail="Skill not found")

    skill_summary = (
        skill_df.groupby("element_name", as_index=False)["data_value"]
        .mean()
        .iloc[0]
    )

    top_occupations = (
        skill_df[["soc_code", "title", "data_value"]]
        .drop_duplicates()
        .sort_values("data_value", ascending=False)
        .head(10)
    )

    occupations = [
        {
            "soc_code": row["soc_code"],
            "title": row["title"],
            "data_value": round(float(row["data_value"]), 2),
        }
        for _, row in top_occupations.iterrows()
    ]

    return {
        "skill_name": skill_summary["element_name"],
        "average_data_value": round(float(skill_summary["data_value"]), 2),
        "top_occupations": occupations,
    }