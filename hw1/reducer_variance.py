#!/usr/bin/env python3
import sys

c = 0
m = 0
v = 0

for line in sys.stdin:
    tup = line.split(sep=' ')
    
    ck = int(tup[0])
    mk = float(tup[1])
    vk = float(tup[2])
    
    v = (c * v + ck * vk) / (c + ck)
    m = (c * m + ck * mk) / (c + ck)
    c += ck
    
print(var)
