import os

file_input = 'input.txt'
file_output = 'reverse.txt'
try:
    fi = open(file_input, 'r')
    fo = open(file_output, 'w')
    list_str = fi.read().split('\n')
    list_str = [i[::-1] for i in list_str]
    list_str.reverse()
    print(list_str)
    for i in list_str:
        fo.write(i + "\n")
except IOError:
    fi = open(file_input, 'w')
    fo = open(file_output, 'w')
# print(f.read)