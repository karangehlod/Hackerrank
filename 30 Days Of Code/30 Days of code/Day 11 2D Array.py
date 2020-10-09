#!/bin/python3

import math
import os
import random
import re
import sys


def perl_sum(mat, row, col):
    sam = 0
    sam += mat[row-1][col-1]
    sam += mat[row-1][col]
    sam += mat[row-1][col+1]
    sam += mat[row][col]
    sam += mat[row+1][col-1]
    sam += mat[row+1][col]
    sam += mat[row+1][col+1]
    return sam


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
# print(arr)
mx = -100
for i in range(1, 5):
    for j in range(1, 5):
        # print(arr[i][j])
        a = perl_sum(arr, i, j)
        if a > mx:
            mx = a
print(mx)
