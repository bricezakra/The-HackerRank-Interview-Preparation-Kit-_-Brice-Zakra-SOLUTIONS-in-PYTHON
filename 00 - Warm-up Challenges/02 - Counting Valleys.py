#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.

## "n" represents the --number of steps-- Gary takes                                                                                  e.g.: n = 8
## "s" represents the string describing --its path-- ("U" for "UP" & "D" for "DOWN")                                                  e.g.: s = ["U", "D", "D", "D", "U", "D", "U", "U"]                                           

def countingValleys(n, s):
    ## Considering our problem on a --Graph (COORDINATE GRAPHIC SYSTEM)--, the --sea level (that we will call here "level_sea")-- will be -- the ABSCISSA axis X starting at 0 (X = 0)-- ...
    ## ... and --"U" & "D"-- will represent --the ALTITUDE-- -- on the ORDINATE axis Y also starting at 0 (Y = 0) and moving forward UP & DOWN (for Y += 1 for "U" OR Y -= 1 for "D")
    ## Starting Point == ORIGIN(X,Y) == (0,0)

    ## a VALLEY is defined as "a sequence of consecutive steps below the --sea level--, starting with a step down from the --sea level-- and ending with a step up to sea level.""...
    ## ... meaning "WE WILL HAVE A VALLEY EVERYTIME WE WILL MEET the --sea level (0)-- COMING FROM THE --BOTTOM--"

    ## let's set our "level_sea" & our "valleyCounter" to 0
    level_sea = valleyCounter = 0
    ## let's set up our LOOP for "i" in --the number of steps "n"-- Gary takes
    for i in range (n):
        ## If "i" belongs to the --string "s" and is equal to "U", ...
        if (s[i] == "U"):
            ## ... the --sea level-- will increment by 1
            level_sea += 1
            ## Since s[i] == "U" in this LOOP (meaning Gary is going up), if the --level_sea == 0--, it also means that is "GARY IS COMING UP FROM --BELOW THE "SEA LEVEL"--"...
            if (level_sea == 0):
                ## ..., therefore the "valleyCounter" will INCREMENT by 1 eveytime --GARY REACHES THE SEA LEVEL when it is equal to 0 (level_sea == 0) --COMING FROM THE BOTTOM--. 
                valleyCounter += 1
        ## else, (meaning if s[i] == "D") ...
        else:
            ## ... the --sea level-- will decrement by 1 
            level_sea -= 1
    ## let's return our "valleyCounter" to get the exact amount of --VALLEYS-- in our -- ARRAY of string--
    return valleyCounter
   
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
