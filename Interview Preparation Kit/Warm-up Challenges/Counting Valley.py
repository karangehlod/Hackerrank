#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    c = 0

    count = 0
    for i in range(0, steps):
        if path[i] == "U":
            count += 1
            print(count)
            if count == 0:
                c += 1
            continue
        elif path[i] == "D":
            count -= 1

            print(count)
            continue

    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
