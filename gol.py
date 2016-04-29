import time
import random
import os
class W:
    t = 0
    x = [0,30]
    y = [0,30]
    c = []
    f = []
    def sf():
        rx = random.randint(0,30)
        ry = random.randint(0,30)
        W.f.append(F(rx,ry))
    def pt():
        W.t += 1
        W.sf()
        for c in W.c:
            c.l()
            c.m()
            c.ea()
            c.s()
class F:
    def __init__(self,x,y):
        self.e = 250
        self.x = x
        self.y = y
class C:
    cid = 0
    def __init__(self,x,y,e):
        self.cid = C.cid
        C.cid += 1
        self.e = e
        self.x = x
        self.y = y
    def mr(self):
        if self.x < W.x[1]:
            self.x += 1
    def ml(self):
        if self.x > W.x[0]:
            self.x -= 1
    def md(self):
        if self.y < W.y[1]:
            self.y += 1
    def mu(self):
        if self.y > W.y[0]:
            self.y -= 1
    def ea(self):
        for f in W.f:
            if f.x == self.x and f.y == self.y:
                self.e += f.e
                W.f.remove(f)
    def m(self):
        r = random.randint(0,3)
        if r == 0:
            self.mr()
        elif r == 1:
            self.ml()
        elif r == 2:
            self.md()
        elif r == 3:
            self.mu()
    def d(self):
        for c in W.c:
            if c.cid == self.cid:
                W.c.remove(c)
    def l(self):
        if self.e > 0:
            self.e -= 5
        else:
            self.d()
    def s(self):
        if self.e >= 500:
            self.e = self.e / 2
            W.c.append(C(self.x,self.y,self.e))
def dr():
    os.system("clear")
    for y in range(W.y[1]):
        print()
        for x in range(W.x[1]):
            pc = False
            fc = False
            for c in W.c:
                if c.x == x and c.y == y:
                    pc = True
            if pc:
                print("o",end='')
            else:
                for f in W.f:
                    if f.x == x and f.y == y:
                        fc = True
                if fc:
                    print("x",end='')
                else:
                    print(".",end='')
    print()
def main():
    W.c.append(C(15,15,250))
    while True:
        time.sleep(.1)
        dr()
        #print("C: " + str(len(W.c)))
        #print("F: " + str(len(W.f)))
        W.pt()
main()
