from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth, habits, workouts

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MomentumX API",
    description="Backend for MomentumX fitness tracking app",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(habits.router)
app.include_router(workouts.router)

@app.get("/")
def root():
    return {
        "app": "MomentumX API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}