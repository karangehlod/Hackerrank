#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.


def factorial(n):
    op = 1
    if n == 1:
        return op
    elif n > 1 and n < 13:
        while(n != 1):
            op = op*n
            n = n-1
    return op


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
