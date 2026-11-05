from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Optional
import os
from .services import agriculture

BASE = Path(__file__).resolve().parent

app = FastAPI(title="AgriCare AI", version="2.0.0",
              description="Smart farming assistant with modular agriculture tools")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE / "static" / "index.html").read_text(encoding="utf-8")

class FertilizerInput(BaseModel):
    crop: str
    nitrogen: float = Field(ge=0, le=500)
    phosphorus: float = Field(ge=0, le=500)
    potassium: float = Field(ge=0, le=500)
    ph: float = Field(ge=0, le=14)
    soil_type: str = "Loamy"

class TwinInput(BaseModel):
    crop: str = "Tomato"
    area_acres: float = Field(default=1, gt=0, le=10000)
    soil_moisture: float = Field(default=35, ge=0, le=100)
    temperature_c: float = Field(default=30, ge=-10, le=60)
    irrigation_percent: float = Field(default=100, ge=0, le=200)
    days: int = Field(default=7, ge=1, le=90)

class AssistantInput(BaseModel):
    question: str
    language: str = "English"

@app.get("/api/health")
def health():
    return {"status": "ok", "application": "AgriCare AI", "version": "2.0.0"}

@app.post("/api/fertilizer/recommend")
def fertilizer(data: FertilizerInput):
    return agriculture.fertilizer_recommendation(data.model_dump())

@app.post("/api/pest/detect")
async def pest_detect(image: UploadFile = File(...)):
    allowed = {"image/jpeg", "image/png", "image/webp"}
    if image.content_type not in allowed:
        raise HTTPException(400, "Upload a JPG, PNG or WEBP image.")
    if image.size and image.size > 10 * 1024 * 1024:
        raise HTTPException(413, "Image must be smaller than 10 MB.")
    # Do not persist uploads on Vercel: serverless filesystems are temporary.
    # This starter validates the upload but does not run a trained vision model.
    return agriculture.pest_demo_result(image.filename or "uploaded image")

@app.get("/api/market/prices")
def market_prices(crop: str = "Tomato", market: str = "Hyderabad"):
    return agriculture.market_prices(crop, market)

@app.post("/api/digital-twin/simulate")
def digital_twin(data: TwinInput):
    return agriculture.digital_twin(data.model_dump())

@app.post("/api/assistant")
def assistant(data: AssistantInput):
    if not data.question.strip():
        raise HTTPException(400, "Please enter a question.")
    return agriculture.farming_assistant(data.question, data.language)

# Existing-project-style sections are retained as dashboard entry points.
@app.get("/api/dashboard")
def dashboard():
    return agriculture.dashboard_summary()

@app.get("/api/disease/info")
def disease_info(crop: str = "Tomato"):
    return agriculture.disease_guidance(crop)

@app.get("/api/irrigation/advice")
def irrigation_advice(moisture: float = 35):
    if not 0 <= moisture <= 100:
        raise HTTPException(400, "Moisture must be between 0 and 100.")
    return agriculture.irrigation_advice(moisture)
