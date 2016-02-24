import random
import time
import sys

hex_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def info():
    print("""Usage: hash.py -a <algorithm>
    r: python built-in random
    l: lsa""")

def lsa():
    return int(int(str(time.time())[-1])+int(str(time.time())[-2])/1.25)-1

def gen_hash(mode):
    my_hash = ""
    if mode == "random":
        for i in range(32):
            my_hash += random.choice(hex_list)
        return my_hash
    elif mode == "lsa":
        for i in range(32):
            rnd = lsa()
            rnd2 = (rnd + 1) / 1000
            my_hash += hex_list[rnd]
            time.sleep(rnd2)
            while rnd == lsa():
                pass
        return my_hash

if len(sys.argv) > 2:
    if sys.argv[1] == "-a" and sys.argv[2] == "r":
        print(gen_hash("random"))
    elif sys.argv[1] == "-a" and sys.argv[2] == "l":
        print(gen_hash("lsa"))
    else:
        info()
else:
    info()
