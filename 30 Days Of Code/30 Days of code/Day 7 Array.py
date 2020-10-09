#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    for i in range(n, 0, -1): #for reverese -1 with start n and end 0
        print(arr[i-1], end=' ')
