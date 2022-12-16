#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    result=[]
    if (len(grades)>=1 and len(grades)<=60):
        for g in grades:
            if (g>=0 and g<=100):
                if g < 38:
                    result.append(g)
                else:
                    mul=((g+5)//5)*5
                    if mul-g<3:
                        result.append(mul)
                    else:
                        result.append(g)
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
