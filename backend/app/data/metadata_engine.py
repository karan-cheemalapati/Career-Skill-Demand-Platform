def get_filter_metadata_data(df):
    skills = sorted(
        df["element_name"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    education_levels = sorted(
        df["preferred_education"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    )

    return {
        "skills": skills,
        "education_levels": education_levels
    }