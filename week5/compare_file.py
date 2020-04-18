import os

filenameA = 'a.txt'
filenameB = 'b.txt'

def compare_file(a, b):
    return a == b

try:
    fa = open(filenameA, 'r')
    fb = open(filenameB, 'r')
    a = fa.readlines()
    b = fb.readlines()
    print(a, b, sep="\n")
    print(compare_file(a, b))
except IOError:
    print("not exist: " + filenameA + " or " + filenameB)