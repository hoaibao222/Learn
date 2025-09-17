import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from datetime import timedelta

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="71cd9e939ccd445c965118b8c74b237c",
    client_secret="101602a6a49043b5a7bbbd6cc78780d3",
    redirect_uri="http://127.0.0.1:8000/callback",
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

    while True:
        current = sp.current_playback()
        current_id = current['item']['id']
        if current_id != last_id:
            last_id = current_id
            if current and current['item']:
                track = current['item']
                name = track['name']
                artist = ', '.join([a['name'] for a in track['artists']])
                album = track['album']['name']
                progress_ms = current['progress_ms']
                duration_ms = track['duration_ms']
                progress = str(timedelta(milliseconds=progress_ms)).split('.')[0]
                duration = str(timedelta(milliseconds=duration_ms)).split('.')[0]
                print(f"🎵 Now playing: {name} — {artist}")
                print(f"💿 Album: {album}")
                print(f"⏰ {progress} / {duration}")
                break
            else:
                print("No track is currently playing.")
        else:
                print("Nothing change")
    time.sleep(2)


while True:
    spotify()