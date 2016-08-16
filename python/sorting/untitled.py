#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

maxE = max(a)

sumall = sum(a) - maxE

if len(a) == 1:
    print(2)
elif len(a) == 2 and a[0] == a[1]:
    print(2)
elif maxE >= sumall:
    print(1)
else:
    print(0)