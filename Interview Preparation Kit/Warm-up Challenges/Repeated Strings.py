#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    count = 0
    result = 0
    lengthOfString = len(s)
    remainderc = 0

    for i in range(lengthOfString):
        if(s[i] == 'a'):
            count += 1
    print(count)
    numofullrepeatation = (n//lengthOfString)

    if numofullrepeatation != 0:
        remainder = n-(numofullrepeatation*lengthOfString)
        for x in range(remainder):
            if(s[x] == 'a'):
                remainderc += 1
    elif lengthOfString > n:  # case23
        lengthOfString = n
        for i in range(lengthOfString):
            if(s[i] == 'a'):
                remainderc += 1

    print(numofullrepeatation)
    print(remainderc)
    result = (numofullrepeatation*count)+remainderc
    print(result)
    # for i in range(numofullrepeatation):
    return result


    # print(lengthOfString)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
