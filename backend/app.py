from fastapi import FastAPI
from pydantic import BaseModel
from emotion_model import predict_emotion
from music_prompt import generate_prompt

app = FastAPI()

class MoodInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: MoodInput):
    emotion = predict_emotion(input.text)
    prompt = generate_prompt(input.text, emotion["label"])
    return {
        "input": input.text,
        "emotion": emotion,
        "music_prompt": prompt
    }
