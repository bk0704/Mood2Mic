from fastapi import FastAPI
from pydantic import BaseModel
from emotion_model import predict_emotion
from music_prompt import generate_prompt
from perplexity_api import query_perplexity

app = FastAPI()

class MoodInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: MoodInput):
    emotion = predict_emotion(input.text)
    prompt = generate_prompt(input.text, emotion["label"])
    songs = query_perplexity(prompt)

    return {
        "input": input.text,
        "emotion": emotion,
        "songs": songs
    }
