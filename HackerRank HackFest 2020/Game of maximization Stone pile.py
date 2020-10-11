#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumStones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def maximumStones(arr):
    odd = 0
    even = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            even += arr[i]
        else:
            odd += arr[i]

    while(even != odd):
        if(even > odd):
            even = even-1
        elif even < odd:
            odd = odd-1
    return even*2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
