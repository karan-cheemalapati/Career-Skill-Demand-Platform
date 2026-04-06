from fastapi import FastAPI
from backend.app.routes.skills import router as skills_router
from backend.app.routes.occupations import router as occupations_router

app = FastAPI(title="Career Skill Demand Platform API")

app.include_router(skills_router)
app.include_router(occupations_router)


@app.get("/")
def read_root():
    return {"message": "Backend is running"}