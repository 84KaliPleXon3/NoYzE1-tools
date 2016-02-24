import random
import time
import sys

hex_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

def info():
    print("""Usage: pwgen.py -a <algorithm>
    p: python built-in pseudo-random
    l: lsa""")

def lsa():
    try:
        return int(int(str(time.time())[-1])+int(str(time.time())[-2])/1.25)-1
    except:
        return lsa()

def gen_hash(mode):
    my_hash = ""
    if mode == "py":
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
    if sys.argv[1] == "-a" and sys.argv[2] == "p":
        print(gen_hash("py"))
    elif sys.argv[1] == "-a" and sys.argv[2] == "l":
        print(gen_hash("lsa"))
    else:
        info()
elif len(sys.argv) > 1 and sys.argv[1] == "-debug":
    i = 1
    a = gen_hash("lsa")
    print(a, "0", flush=True)
    b = ""
    while b != a:
        b = gen_hash("lsa")
        print(b, i, flush=True)
        i += 1
else:
    info()
