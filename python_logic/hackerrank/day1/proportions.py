#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
# 
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i < 0:
            pos+=1
        elif i > 0:
            neg+=1
        elif i == 0:
            zer+=1
        
    total = pos + neg + zer
    pos = pos/total
    neg = neg/total
    zer = zer/total
    print("%.6f" % neg)
    print("%.6f" % pos)
    print("%.6f" % zer)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)