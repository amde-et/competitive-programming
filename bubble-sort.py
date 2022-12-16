#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    if (len(a)>=2 and len(a)<=600):
        swaps=0
        for i in range(len(a)-1):
            if(a[i]>=1 and a[i]<=2000000):
                for j in range(i+1,len(a)):
                    if(a[j]>=1 and a[j]<=2000000):
                        if a[i]>a[j]:
                            a[i],a[j]=a[j],a[i]
                            swaps+=1
        print("Array is sorted in "+str(swaps)+" swaps.")
        print("First Element: "+str(a[0]))
        print("Last Element: "+str(a[len(a)-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
