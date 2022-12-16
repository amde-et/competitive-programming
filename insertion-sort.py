#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    if (len(arr)>=1 and len(arr)<=1000):
        tmp=arr[-1]
        i=arr.index(tmp)
        j=len(arr)-2
        while(tmp<arr[j]):
            if(arr[i]>=-10000 and arr[i]<=10000) and (arr[j]>=-10000 and arr[j]<=10000):
                arr[i]=arr[j]
                j-=1
                i-=1
                print(*arr, sep=' ')
                if i==0:
                    break
        arr[i]=tmp
        print(*arr, sep=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
