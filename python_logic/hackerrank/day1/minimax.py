#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

arr=[1,3,5,7,9]
somamax = arr[0]
somamin = arr[0]
soma = 0
"""
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        j+=1
        somamax = somamax + arr[i]
        #soma = arr + 1
        print(somamax)
        #print(j)

"""
for j in arr:
    soma += j
    if j > somamax:
        somamax = j
    if j < min:
        somamin = j
        #print(somamin)

print(somamax,somamin)
#print(somamin)
        
