def generate_prompt(text, emotion):
    return f"""
Suggest 5 rap songs that match the emotion: {emotion.upper()}.
User's mood post: "{text}"

Return only song names and artist names. No explanations.
"""