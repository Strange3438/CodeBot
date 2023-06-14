import math
import os
import random
import re
import sys

def solve(s):
    arr = list(map(str, s.split(" ")))
    a = []
    for i in arr:
        a.append(i.capitalize())
    p = ' '.join(a)
    return p 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
