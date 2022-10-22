#!/usr/bin/env python3
import sys

PRICE_COLUMN = -7

mk = 0
ck = 0

for line in sys.stdin:
    row = line.split(sep=',')
    try:
        price = int(row[PRICE_COLUMN]) 
        mk += price
        ck += 1
    except:
        continue

print(ck, mk / ck)
