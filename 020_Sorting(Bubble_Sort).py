#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
def bubble(n,a):
    count = 0
    for i in range(n):
        for o in range(0,len(a)-1):
            if a[o] > a[o+1]:
                a[o],a[o+1] = a[o+1],a[o]
                count += 1
            else:
                pass
    return count
x = bubble(n,a)


print("Array is sorted in {} swaps.".format(x))
print("First Element: {}".format(min(a)))
print("Last Element: {}".format(max(a)))
