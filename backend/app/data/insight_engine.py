from backend.app.data.skill_mapper import KEYWORD_TO_SKILL
from backend.app.data.text_utils import normalize_text


def analyze_input_text(df, input_text: str):
    available_skills = (
        df["element_name"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    available_skills_set = set(available_skills)
    text_lower = normalize_text(input_text)

    detected_skills = []

    for keyword, mapped_skill in KEYWORD_TO_SKILL.items():
        if keyword in text_lower and mapped_skill in available_skills_set:
            detected_skills.append(mapped_skill)

    detected_skills = list(dict.fromkeys(detected_skills))

    matched_rows = df[df["element_name"].isin(detected_skills)]

    top_occupations = []
    recommended_skills = []

    if not matched_rows.empty:
        grouped = (
            matched_rows.groupby(["soc_code", "title"], as_index=False)["data_value"]
            .mean()
            .sort_values("data_value", ascending=False)
            .head(5)
        )

        top_occupations = [
            {
                "soc_code": row["soc_code"],
                "title": row["title"],
                "average_skill_score": round(float(row["data_value"]), 2),
            }
            for _, row in grouped.iterrows()
        ]

        top_soc_codes = grouped["soc_code"].astype(str).tolist()

        recommendation_rows = df[df["soc_code"].astype(str).isin(top_soc_codes)]

        recommended_grouped = (
            recommendation_rows.groupby("element_name", as_index=False)["data_value"]
            .mean()
            .sort_values("data_value", ascending=False)
        )

        recommended_skills = [
            row["element_name"]
            for _, row in recommended_grouped.iterrows()
            if row["element_name"] not in detected_skills
        ][:5]

    return {
        "detected_skills": detected_skills,
        "recommended_skills": recommended_skills,
        "top_occupations": top_occupations,
    }