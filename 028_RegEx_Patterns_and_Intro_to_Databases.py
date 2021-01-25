#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    l = []

    for N_itr in range(N):

        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        x = emailID.split("@")
        if x[1] == "gmail.com":
            l.append(firstName)

    x = sorted(l)
    for i in x:
        print(i)



