a = open("<path>", "rb")
h = [0x50,0x36,0x0A,0x31,0x39,0x32,0x30,0x20,0x31,0x32,0x30,0x30,0x0A,0x32,0x35,0x35,0x0A]
im = []
for b in a.read():
    if len(im) < (1920 * 1200)*3:
        c = str(bin(b)).lstrip("0b")
        for d in c:
            if d == "0":
                for i in range(3):
                    im.append(0)
            elif d == "1":
                for i in range(3):
                    im.append(255)
while len(im) < (1920 * 1200)*3:
    for i in range(3):
        im.append(0)
a2 = open("<path>", "wb")
a2.write(bytes(h))
a2.write(bytes(im))
