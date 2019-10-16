#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level_sea = valley = 0
    for i in range (n):
        if (s[i] == "U"):
            level_sea += 1
            if (level_sea == 0):
                valley += 1
        else:
            level_sea -= 1
    return valley
   
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     s = input()

#     result = countingValleys(n, s)

#     fptr.write(str(result) + '\n')

#     fptr.close()


    ## TEST 00
n = 8
s = ["U", "D", "D", "D", "U", "D", "U", "U"]
print(countingValleys(n, s))                                        ### ... output ... 1 (meaning 1 valley)





### BIG O NOTATION:

### Time Complexity: O(n);
### Space Complexity: O(n).
