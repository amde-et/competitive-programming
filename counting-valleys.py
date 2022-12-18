#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    tmp=0
    val=0
    sealvl=True
    for i in range(steps):
        if path[i]=="U":
            tmp+=1
        elif path[i]=="D":
            tmp-=1
        if tmp==0:
            sealvl=True
        if sealvl==True and tmp==-1:
            val+=1
            sealvl=False
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
