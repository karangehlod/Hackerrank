#!/bin/python3

import math
import os
import random
import re
import sys

# alternative method
""" import itertools 
def rotLeft(a, d):
    x = len(a)
    i = d-x
    b = []
    b.append(a[i:x])
    b.append(a[0:i])
    a = list(itertools.chain(*b)) """
# Complete the rotLeft function below.


def rotLeft(a, d):
    x = len(a)
    b = []
    b = a[d:x]
    for j in range(d):
        b.append(a[j])
    return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
