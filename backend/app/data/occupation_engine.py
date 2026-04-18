def get_occupation_detail_data(df, soc_code: str):
    occupation_df = df[df["soc_code"].astype(str) == str(soc_code)].copy()

    if occupation_df.empty:
        return {
            "soc_code": soc_code,
            "found": False,
            "message": "Occupation not found"
        }

    first_row = occupation_df.iloc[0]

    top_skills_df = (
        occupation_df[["element_name", "data_value"]]
        .dropna()
        .drop_duplicates()
        .sort_values("data_value", ascending=False)
        .head(10)
    )

    top_skills = [
        {
            "skill_name": row["element_name"],
            "skill_score": round(float(row["data_value"]), 2),
        }
        for _, row in top_skills_df.iterrows()
    ]

    return {
        "found": True,
        "soc_code": str(first_row["soc_code"]),
        "title": first_row["title"],
        "description": None if str(first_row.get("description", "")) == "nan" else first_row.get("description"),
        "a_mean": None if str(first_row.get("a_mean", "")) == "nan" else float(first_row["a_mean"]),
        "a_median": None if str(first_row.get("a_median", "")) == "nan" else float(first_row["a_median"]),
        "tot_emp": None if str(first_row.get("tot_emp", "")) == "nan" else float(first_row["tot_emp"]),
        "preferred_education": None if str(first_row.get("preferred_education", "")) == "nan" else first_row.get("preferred_education"),
        "preferred_edu_pct": None if str(first_row.get("preferred_edu_pct", "")) == "nan" else float(first_row["preferred_edu_pct"]),
        "top_skills": top_skills
    }