#!/usr/bin/env python3
import sys

cj = 0
mj = 0

for line in sys.stdin:
    pair = line.split(sep=' ')
    ck = int(pair[0])
    mk = float(pair[1])
    
    mj = (cj * mj + ck * mk) / (cj + ck)
    
    cj += ck

print(mj)
