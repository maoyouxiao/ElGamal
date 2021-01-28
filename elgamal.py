#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from Crypto.Util.number import getPrime

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gen_key(p):
    key = random.randint(2, p-2)
    while gcd(key, p) != 1:
        key = random.randint(2, p-2)
    return key

class ElGamal:

    def __init__(self, p=-1, g=-1, y=-1, k=-1):
        self.p = p
        self.g = g
        self.y = y
        self.k = k

    def generate(self, num):
        self.p = getPrime(num)
        #self.g = gen_key(self.p)
        self.g = random.randint(2, self.p-2)
        #self.k = gen_key(self.p)
        self.k = random.randint(2, self.p-2)
        self.y = pow(self.g, self.k, self.p)
        return self.p, self.g, self.y, self.k

    def encrypt(self, msg, p=-1, g=-1, y=-1):
        if p < 0:
            p = self.p
        if g < 0:
            g = self.g
        if y < 0:
            y = self.y
        if p < 0 or g < 0 or y < 0:
            raise Exception("p or g or y missed")

        #r = gen_key(p)
        r = random.randint(2, p-2)
        K = pow(y, r, p)
        c1 = pow(g, r, p)
        c2 = [c * K for c in msg]
        return c1, c2

    def decrypt(self, c1, c2, p=-1, k=-1):
        if p < 0:
            p = self.p
        if k < 0:
            k = self.k
        if p < 0 or k < 0:
            raise Exception("p or k missed")

        K = pow(c1, k, p)
        return bytes([c // K for c in c2])

def test():
    msg = b"i love you, baby"
    e = ElGamal()
    e.generate(512)

    print("P =", e.p)
    print("G =", e.g)
    print("Y =", e.y)
    print("K =", e.k)

    c1, c2 = e.encrypt(msg)
    print("C1 =", c1)
    print("C2 =", c2)
    m = e.decrypt(c1, c2)
    print("m =", m)

def brute():
    import sys
    e = ElGamal()
    # if p is small, can brute
    e.generate(16)
    p = e.p
    g = e.g
    y = e.y
    print("p =", p)
    print("g =", g)
    print("y =", y)
    e = None

    # hide cursor
    sys.stdout.write("\033[?25l")
    print("Bruting...")
    for k in range(0, p):
        sys.stdout.write("Trying => k = %d\r" % k)
        if (pow(g, k, p) == y):
            break
        if k == p-1:
            print("\nFailed...")
            return
    print("\nTesting...")
    msg = b"fuck you, baby"
    print("Test Message:", msg)
    e = ElGamal()
    c1, c2 = e.encrypt(msg, p, g, y)
    print("c1 =", c1)
    print("c2 =", c2)
    m = e.decrypt(c1, c2, p, k)
    print("Get Message:", m)
    # reset cursor
    sys.stdout.write("\033[?25h")

if __name__ == "__main__":
    #test()
    brute()
