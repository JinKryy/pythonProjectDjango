import time
from .models import URL

def timer(time_min, pk):
    time_sec = time_min * 60
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}: {:02d}'.format
        (mins, secs)
        time.sleep(1)
        time_sec -= 1
    URL.objects.filter(id=pk).delete()

