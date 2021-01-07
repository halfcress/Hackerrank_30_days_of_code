#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    count = 0
    y = (str(bin(n)[2:]))
    x = y.split("0")
    x = sorted(x)
    ozan = x[-1]

    for i in ozan:
        if i == "1":
            count += 1

    print(count)