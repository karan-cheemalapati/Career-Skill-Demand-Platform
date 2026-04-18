from backend.app.data.questions_engine import get_guided_questions_data
from backend.app.data.metadata_engine import get_filter_metadata_data


def get_insights_summary_data(df):
    metadata = get_filter_metadata_data(df)
    questions = get_guided_questions_data()

    top_occupations_df = (
        df[["soc_code", "title", "a_mean", "a_median", "tot_emp", "preferred_education"]]
        .drop_duplicates()
        .sort_values("a_mean", ascending=False)
        .head(10)
    )

    top_occupations = [
        {
            "soc_code": row["soc_code"],
            "title": row["title"],
            "a_mean": None if str(row["a_mean"]) == "nan" else float(row["a_mean"]),
            "a_median": None if str(row["a_median"]) == "nan" else float(row["a_median"]),
            "tot_emp": None if str(row["tot_emp"]) == "nan" else float(row["tot_emp"]),
            "preferred_education": None if str(row["preferred_education"]) == "nan" else row["preferred_education"],
        }
        for _, row in top_occupations_df.iterrows()
    ]

    return {
        "questions": questions["questions"],
        "skills": metadata["skills"],
        "education_levels": metadata["education_levels"],
        "top_occupations": top_occupations,
    }