import time
import os
import sys

for arg in sys.argv:
    if arg == "-v":
        verbose = True
    else:
        verbose = False

def get_now():
        now = time.localtime().tm_hour * 60 * 60
        now += time.localtime().tm_min * 60
        now += time.localtime().tm_sec
        now += time.time() - int(time.time())
        return now

def calc_left(now):
    return 61800 - now

def get_percent(now):
    return ((30600 - calc_left(now)) / 30600) * 100

def render_bar(value):
    bar = "["
    bar += "#" * int(value / 5)
    bar += " " * (20 - int(value / 5))
    bar += "] "
    return bar

while True:
    time.sleep(.1)
    value = round(get_percent(get_now()),3)
    if not verbose:
        os.system("cls")
    print(render_bar(value),value,"%",sep="")
    if value >= 100:
        print("Done!")
        break
