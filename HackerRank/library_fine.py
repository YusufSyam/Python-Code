#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#
def get_day(d, m=0, y=0):
    return d+(m*30)+(y*365)

def libraryFine(d1, m1, y1, d2, m2, y2):
    if get_day(d1, m1, y1) <= get_day(d2, m2, y2):
        return 0
    else:
        if y1>y2:
            return 10000
        else:
            if m1==m2:
                return 15*abs(d1-d2)
            else:
                if get_day(d1, m1) <= get_day(d2, m2):
                    return 0
                else:
                    return 500*abs(m1-m2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])
    
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    fptr.write(str(result) + '\n')

    fptr.close()
