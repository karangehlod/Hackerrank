#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):

    cost1 = meal_cost*(tip_percent/100)
    # print(cost1)
    cost2 = meal_cost*(tax_percent/100)
    # print(cost2)
    cost = round(meal_cost+cost1+cost2)
    print(cost)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
