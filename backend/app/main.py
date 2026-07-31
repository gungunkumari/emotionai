from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.predict import router as predict_router
from backend.app.api.routes.prediction_routes import router as prediction_router
from backend.app.api.routes.dashboard_routes import router as dashboard_router

from backend.app.db.database import Base, engine

import backend.app.models

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EmotionSense AI API",
    version="1.0.0",
    description="Deep Learning-Based Facial Emotion Recognition API",
    contact={
        "name": "Saanvi Kumari",
        "email": "your_email@example.com"
    },
    license_info={
        "name": "MIT"
    }
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")
# Register Routes
app.include_router(health_router)
app.include_router(predict_router)
app.include_router(prediction_router)
app.include_router(dashboard_router)


@app.get("/api-info", tags=["API"])
def api_info():
    return {
        "project": "EmotionSense AI",
        "version": "1.0.0",
        "status": "Running",
        "framework": "FastAPI",
        "database": "PostgreSQL",
        "model": "CNN Emotion Recognition"
    }