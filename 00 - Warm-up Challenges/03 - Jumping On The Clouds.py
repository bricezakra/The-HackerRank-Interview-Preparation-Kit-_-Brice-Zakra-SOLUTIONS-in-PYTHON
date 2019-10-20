#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # let's set Emma's initial position to index[0]
    currentPosition = 0
    # let's set our jumpCounter to 0
    jumpCounter = 0

    # Our currentPosition index starts at 0, as long as it is less than the LENGTH (len(c)) of our list -1, ...
    while currentPosition < len(c) - 1:
        # Since Emma can jump any cumulus from her currentPosition +1 or +2 & that is not a thunderhead cloud 1, ...
        if currentPosition + 2 < len(c) and c[currentPosition + 2] != 1:
            # ...her position will increment by one as long as the condition is respected in this loop.
            currentPosition += 1
        # ... Emma's position will increment.
        currentPosition += 1
        # ... our jumperCounter will increment as well.
        jumpCounter += 1
    # Let's return our jumpCounter 
    return jumpCounter

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     c = list(map(int, input().rstrip().split()))

#     result = jumpingOnClouds(c)

#     fptr.write(str(result) + '\n')

#     fptr.close()


##Test00
n = 9                                                  ## "n" is the lenght of our list
c = [0 , 1, 0, 0, 0, 0, 1, 0, 0]                       ## "c" is our list
print(jumpingOnClouds(c))                              ## ... output ... 5





### BIG O NOTATION:

### Time Complexity: ;
### Space Complexity: .
