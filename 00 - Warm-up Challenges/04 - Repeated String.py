#!/bin/python3

import math
import os
import random
import re
import sys


s = ["a","b","a"]                                         ## switch -----s = ["a","b","a"]----- for -----s = input()----- to run the solution on HackerRank
n = 10                                                    ## switch -----n = 10----- for -----n = int(input())----- to run the solution on HackerRank

counterOfa = 0
length = len(s)
len = length

for i in range (len):
    if s[i] == "a":
        counterOfa += 1

count_string = n//len
repeatedString = count_string * counterOfa
x = count_string * len

i = 0
while x < n:
    if s[i] == "a":
        repeatedString += 1
        x += 1
    else:
        x += 1
    i += 1

print(repeatedString)                                      ## ... output ... 7                           



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()