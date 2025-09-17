# Install this library by running: pip install spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-modify-playback-state,user-read-playback-state"
))
last_id = None

def spotify():
    global last_id

    print("Spotify controller:\n1. Resume song\n2. Pause song\n3. Previous song\n4. Next song")
    choice = int(input("Select number: "))

    if choice == 1:
        try:
            sp.start_playback()
        except Exception:
            pass
    elif choice == 2:
        try:
            sp.pause_playback()
        except Exception:
            pass
    elif choice == 3:
        try:
            sp.previous_track()
        except Exception:
            pass
    elif choice == 4:
        try:
            sp.next_track()
        except Exception:
            pass
    else:
        print("Invalid choice.")

    last_playing = None
    max_retries = 5
    for attempt in range(max_retries):
        current = sp.current_playback()
        if current and current['item']:
            current_id = current['item']['id']
            is_playing = current['is_playing']
            if current_id != last_id or is_playing != last_playing:
                track = current['item']
                name = track['name']
                artist = ', '.join([a['name'] for a in track['artists']])
                album = track['album']['name']
                progress_ms = current['progress_ms']
                duration_ms = track['duration_ms']
                progress = str(timedelta(milliseconds=progress_ms)).split('.')[0]
                duration = str(timedelta(milliseconds=duration_ms)).split('.')[0]
                state = "▶️ Playing" if is_playing else "⏸️ Paused"
                print(f"🎵 Now playing: {name} — {artist}")
                print(f"💿 Album: {album}")
                print(f"⏰ {progress} / {duration}")
                print(f"{state}")
                last_id = current_id
                last_playing = is_playing
                break
            else:
                if attempt == max_retries - 1:
                    print("Nothing change")
        else:
            if attempt == max_retries - 1:
                print("No track is currently playing.")


while True:
    spotify()