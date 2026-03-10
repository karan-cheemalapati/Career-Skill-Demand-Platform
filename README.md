# Career & Skill Demand Intelligence Platform

An interactive big data analytics platform that processes the U.S. labor market data to help users understand which skills are most in demand, which occupations pay the best, and what education level is typically required for different careers.

---

## Project Overview

The Career & Skill Demand Intelligence Platform analyzes data from **O\*NET** and the **Bureau of Labor Statistics (BLS)** to surface meaningful insights about the U.S. job market. The processed data is served through a **FastAPI backend** and displayed on an **interactive dashboard** where users can explore skill demand, occupation salaries, and education requirements.

### What users can explore on the dashboard:
- **Top in-demand skills** across all U.S. occupations
- **Top paying occupations** nationally
- **Education level** typically required per occupation
- **Skill demand scores** — how widely required a skill is
- **Salary comparisons** across different career paths
- **Relationship between skills, education, and salary**

---

## Data Pipeline

```
O*NET + BLS Raw Datasets
        |
Data Cleaning & Preparation
(Pandas, Jupyter Notebook)
        |
PySpark ETL & Analytics 
(Compute metrics, load to BigQuery)
        |
FastAPI Backend      
(Serve data via REST APIs)
        |
Interactive Dashboard      
(Streamlit / React frontend)
```

---

## Project Structure

```
Career-Skill-Demand-Platform/
├── data/
│   ├── cleaned_data/      # Cleaned and processed datasets output by ingestion
│   └── raw_data/          # Original downloaded datasets (O*NET + BLS)
├── notebooks/             # Jupyter notebooks for EDA and data cleaning
├── src/
│   ├── analysis/          # Skill demand and wage analysis scripts
│   ├── ingestion/         # Data loading and cleaning scripts
│   └── processing/        # PySpark ETL and feature engineering
├── docs/                  # Data dictionary and project documentation
├── tests/                 # Unit tests
├── .gitignore
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Datasets

| Dataset | Source | Description |
|---|---|---|
| `Skills.xlsx` | O\*NET Online | Skill importance and level scores per occupation |
| `Occupation_Data_BDA.xlsx` | O\*NET Online | Occupation titles and descriptions |
| `Education.xlsx` | O\*NET Online | Required education levels per occupation (categories 1–12) |
| `national_M2024_dl.xlsx` | Bureau of Labor Statistics | National employment counts and wage distributions (May 2024) |

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Data Exploration | Python, Pandas, Jupyter Notebook | EDA, cleaning, and preparation |
| Data Processing | PySpark (Apache Spark) | Large-scale ETL and metric computation |
| Cloud Storage | Google Cloud Storage (GCS) | Store raw and processed data files |
| Data Warehouse | Google BigQuery | Store analytics tables, run SQL queries |
| Backend API | FastAPI (Python) | Serve processed data to the frontend |
| Frontend | Streamlit / React | Interactive dashboard and visualizations |
| Containerization | Docker | Package and deploy services consistently |
| Deployment | Google Cloud Run | Host backend and frontend containers |
| Version Control | Git & GitHub | Code collaboration and version management |

---

## Quickstart

```bash
# Clone the repo
git clone https://github.com/karan-cheemalapati/Career-Skill-Demand-Platform.git
cd Career-Skill-Demand-Platform

# Install dependencies
pip install -r requirements.txt

# Run data preparation script
python src/ingestion/data_preparation.py

# Open the EDA and cleaning notebook
jupyter notebook notebooks/BDA_Project_Data_Cleaning_Final.ipynb
```

---

## Task Progress

### Karan — Data Preparation & Ingestion
- Organize and load datasets (O\*NET + BLS)
- Explore datasets using Pandas / Jupyter Notebook
- Identify and document important columns
- Clean column names and formats
- Standardize SOC Codes (remove .00 from O\*NET)
- Extract preferred education level per occupation
- Create data dictionary
- Push cleaned datasets to GitHub
- Upload raw and cleaned datasets to Google Cloud Storage (GCS)

### Veerababu — Data Processing & Metrics (Spark)
- Write PySpark ETL scripts
- Merge Skills, Occupation, Education, and BLS datasets
- Filter for Skill Importance (Scale ID = IM)
- Compute Skill Demand Score and Salary Impact Score
- Output processed datasets as Parquet/CSV
- Upload processed data to GCS
- Load results into BigQuery tables (`skills_metrics`, `occupation_metrics`, `occupations_clean`)

### Sudeep, Alex — Backend Development
- Set up FastAPI project structure
- Connect backend to BigQuery
- Create API endpoints:
  - `GET /top-skills`
  - `GET /skill/{name}`
  - `GET /top-occupations`
  - `GET /occupation/{id}`
- Test APIs locally
- Dockerize backend
- Deploy backend on Cloud Run

### Ajay, Alex — Frontend & Visualization
- Design dashboard layout
- Build UI using Streamlit or React
- Integrate with backend APIs
- Create visualizations:
  - Top skills chart
  - Occupation salary comparison
  - Skill demand ranking
  - Education level vs salary
- Deploy frontend to Cloud Run / Firebase Hosting

### Shared Tasks (Everyone)
- GitHub repository setup
- Folder structure
- Documentation
- Final report
- Presentation slides
- Testing

---

## Team

| Name | Role |
|---|---|
| Karan Cheemalapati | Data Preparation & Ingestion |
| Veerababu Addanki | Data Processing & Metrics (PySpark) |
| Benarjee Sudeep Sampath Pyla | Backend Development (FastAPI) |
| Alex Savard | Backend & Frontend |
| Ajay Tata | Frontend & Visualization |

---

## License

This project is for academic purposes as part of a Big Data course.
