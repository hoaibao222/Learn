from datetime import datetime
import vlc
import time

h, m = map(int, input("Set arlam: ").split())
triggered = False

while triggered == False:
    now = datetime.now()
    if h==now.hour and m==now.minute:
        print("Wake the fuck up")
        sound = vlc.MediaPlayer("C:/Users/Albys/Downloads/gnx.mp3")
        sound.play()
        triggered = True
    time.sleep(1)

while sound.is_playing():
    pass