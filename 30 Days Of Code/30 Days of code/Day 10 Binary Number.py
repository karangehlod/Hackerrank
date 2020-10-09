#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    result = 0
    count = 0
    while(n != 0):
        r = n % 2  # bit generator
        n = n//2  # next step n
        if r == 1:
            count += 1
            result = max(result, count)
        else:
            count = 0
    print(result)
