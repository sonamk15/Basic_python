 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    m = l = scores[0]
    cm = cl = 0
    for i in scores:
        if i > m:
            cm += 1
            m = i
        if i < l:
            cl += 1
            l = i
    return cm, cl

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# "https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem"

