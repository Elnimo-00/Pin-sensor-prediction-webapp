from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tempfile, os

from dataset import load_dataset
from model import train_model, predict_digit

app = FastAPI()

# allow plain HTML access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictIn(BaseModel):
    features: list[float]

@app.post("/train")
async def train(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        path = tmp.name

    X, y = load_dataset(path)
    os.unlink(path)

    if len(X) < 50:
        return {"error": "dataset too small"}

    acc = train_model(X, y)
    return {"samples": len(X), "accuracy": round(acc, 4)}

@app.post("/predict")
def predict(data: PredictIn):
    if len(data.features) != 6:
        return {"error": "need 6 features"}

    digit, conf = predict_digit(data.features)
    return {"digit": digit, "confidence": round(conf, 4)}
