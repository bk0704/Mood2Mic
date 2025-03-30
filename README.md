
# Mood2Mic

Turn your mood into a personalized rap playlist using AI-powered emotion detection.

[![Hugging Face](https://img.shields.io/badge/model-huggingface-blue?logo=huggingface)](https://huggingface.co/bk-0704/mood2mic-emotion-model)



## Overview
**Mood2Mic** is a music discovery app that lets you type your current mood like a tweet — and instantly returns a playlist of rap songs that match your emotional vibe.

It combines emotion analysis, AI-generated music prompts, and real-time search from Spotify, YouTube, and Apple Music.

The result? A personalized rap playlist that feels just right.

The app pulls predictions from our hosted model:  
[https://huggingface.co/bk-0704/mood2mic-emotion-model](https://huggingface.co/bk-0704/mood2mic-emotion-model)
## Features

- 🧠 Emotion detection from tweet-style mood input
- 🎤 Real-time rap playlist generation
- 🔍 AI-powered music search using Perplexity.ai
- 🎧 Cross-platform links: Spotify, YouTube, Apple Music
- 🎨 Clean, Spotify-inspired UI


## How It Works

1. You enter a short mood message (like a tweet)
2. The fine-tuned NLP model(refer to the model on the hugging face link) detects your emotional tone
3. A music prompt is generated using the emotion
4. We fetch matching rap songs using AI search
5. The playlist is displayed with links to multiple platforms

## Model

We fine-tuned the [cardiffnlp/twitter-roberta-base-emotion](https://huggingface.co/cardiffnlp/twitter-roberta-base-emotion) model to also classify the emotions of various rap lyrics

- **Base Model:** twitter-roberta-base-emotion (trained on 58M tweets)
- **Fine-tuning:** A dataset of rap lyrics classified as joy/optimism/anger/sadness
- **Output:** Label + confidence (e.g., "joy", 92.1%)
- **Framework:** HuggingFace Transformers

The emotion label is then used to generate a music search prompt via Perplexity.ai.

👉 You can view and test our fine-tuned model here:  
🔗 [bk-0704/mood2mic-emotion-model](https://huggingface.co/bk-0704/mood2mic-emotion-model)
## Tech Stack

**Frontend:**  
- HTML, CSS (Spotify-inspired), JavaScript

**Backend:**  
- Node.js + Express  
- Python (for model inference)  
- HuggingFace Transformers

**APIs:**  
- Perplexity.ai (music discovery results)  



## License

[MIT](https://choosealicense.com/licenses/mit/)

