from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routes.skills import router as skills_router
from backend.app.routes.occupations import router as occupations_router

app = FastAPI(title="Career Skill Demand Platform API")

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://veerababu33.web.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(skills_router)
app.include_router(occupations_router)


@app.get("/")
def read_root():
    return {"message": "Backend is running"}