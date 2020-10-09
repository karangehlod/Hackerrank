#!/bin/python3

import sys

n = int(input().strip())  # no of elements in array
a = list(map(int, input().strip().split(' ')))  # array elements
# Write Your Code Here
sort = 0
for j in range(n):
    for i in range(n):
        if i < (len(a)-1) and a[i] > a[i+1]:
            sort += 1
            a[i], a[i+1] = a[i+1], a[i]
        elif i == n and (a[0] > a[i]):
            sort += 1
            a[0], a[i] = a[i], a[0]
print("Array is sorted in {} swaps.".format(sort))
print("First Element:", a[0])
print("Last Element:", a[-1])
