import os
import sys

# Add current folder and parent folder to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

sys.path.append(current_dir)
sys.path.append(parent_dir)

from fastapi import FastAPI
from pydantic import BaseModel
from emotion_model import predict_emotion
from music_prompt import generate_prompt
from perplexity_api import query_perplexity
from utils import linkify_songs




app = FastAPI()

class MoodInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: MoodInput):
    emotion = predict_emotion(input.text)
    prompt = generate_prompt(input.text, emotion["label"])
    raw_songs = query_perplexity(prompt)
    links = linkify_songs(raw_songs)

    return {
        "input": input.text,
        "emotion": emotion,
        "results": links
    }

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
