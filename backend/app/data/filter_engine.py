def filter_occupations_data(
    df,
    skill=None,
    min_salary=None,
    min_skill_score=None,
    education=None
):
    filtered_df = df.copy()

    if skill:
        skill_clean = skill.strip().lower()
        filtered_df = filtered_df[
            filtered_df["element_name"].astype(str).str.strip().str.lower() == skill_clean
        ]

    if min_salary is not None:
        filtered_df = filtered_df[
            filtered_df["a_mean"].notna() &
            (filtered_df["a_mean"].astype(float) >= min_salary)
        ]

    if min_skill_score is not None:
        filtered_df = filtered_df[
            filtered_df["data_value"].notna() &
            (filtered_df["data_value"].astype(float) >= min_skill_score)
        ]

    if education:
        education_clean = education.strip().lower()
        filtered_df = filtered_df[
            filtered_df["preferred_education"].astype(str).str.strip().str.lower() == education_clean
        ]

    if filtered_df.empty:
        return []

    grouped = (
        filtered_df.groupby(["soc_code", "title"], as_index=False)
        .agg({
            "data_value": "mean",
            "a_mean": "first",
            "a_median": "first",
            "tot_emp": "first",
            "preferred_education": "first"
        })
        .sort_values(["data_value", "a_mean"], ascending=[False, False])
        .head(20)
    )

    results = [
        {
            "soc_code": row["soc_code"],
            "title": row["title"],
            "skill_score": round(float(row["data_value"]), 2) if str(row["data_value"]) != "nan" else None,
            "a_mean": None if str(row["a_mean"]) == "nan" else float(row["a_mean"]),
            "a_median": None if str(row["a_median"]) == "nan" else float(row["a_median"]),
            "tot_emp": None if str(row["tot_emp"]) == "nan" else float(row["tot_emp"]),
            "preferred_education": None if str(row["preferred_education"]) == "nan" else row["preferred_education"],
        }
        for _, row in grouped.iterrows()
    ]

    return results