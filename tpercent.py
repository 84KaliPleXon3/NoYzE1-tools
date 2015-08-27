import time
import os

def get_now():
        now = time.localtime().tm_hour * 60 * 60
        now += time.localtime().tm_min * 60
        now += time.localtime().tm_sec
        return now

def calc_left(now):
    return 61800 - now

def get_percent(now):
    return ((30600 - calc_left(get_now())) / 30600) * 100

def render_bar(value):
    bar = "["
    bar += "#" * int(value / 5)
    bar += " " * (20 - int(value / 5))
    bar += "] "
    return bar

while True:
    time.sleep(1)
    value = round(get_percent(get_now()),2)
    os.system("cls")
    print(render_bar(value),value,"%",sep="")
