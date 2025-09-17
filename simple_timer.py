from datetime import datetime, timedelta
import vlc
import time

triggered = False
h = int(input("How many hours: "))
m = int(input("How many minutes: "))
s = int(input("How many seconds: "))
presettime = datetime.now() + timedelta(hours=h, minutes=m, seconds=s)
print(f"Arlam starting at {presettime.strftime("%H")}:{presettime.strftime("%M")}:{presettime.strftime("%S")}")

while triggered == False:
    if presettime <= datetime.now():
        sound = vlc.MediaPlayer("C:/Users/Albys/Downloads/gnx.mp3")
        sound.play()
        triggered = True
    time.sleep(1)

while sound.is_playing():
    pass
