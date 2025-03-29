import urllib.parse

def linkify_songs(song_text: str):
    links = []
    lines = song_text.strip().splitlines()
    
    for line in lines:
        line = line.strip("1234567890. ").strip()
        if not line:
            continue

        # Clean & encode song for URL
        query = urllib.parse.quote_plus(line)

        links.append({
            "title": line,
            "youtube": f"https://www.youtube.com/results?search_query={query}",
            "spotify": f"https://open.spotify.com/search/{query}",
            "apple": f"https://music.apple.com/us/search?term={query}"
        })

    return links
