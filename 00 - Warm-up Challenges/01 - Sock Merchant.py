#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.

## "n" represents the number of socks;                                                     ### e.g.: n = 9
## "ar" represents the LIST of array containing the color of each sock;                    ### e.g.: ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]                       

def sockMerchant(n, ar):
    ## We will use the "list(set(...))" method to gather the --different colors-- we have in the array by their --unique number--
    unique_numbers = list(set(ar))
    ## let's test it by returning "unique_numbers" right after using the "list(set(...))" method! It is not necessary for our code. We will do it for good practice and as a debugger, then we will comment it out.
    # return unique_numbers                                                                ### The --output-- should be "[10, 20, 50, 30]""
    ## Now let's set the --total pairs-- in our LIST of array to "0"!
    total_pairs = 0
    ## Let's set our LOOP for how many times we can find a --specific number "n"-- in our --set-- of --unique numbers--!
    for n in unique_numbers:
        ## Since "total_pairs" has been set to "0" before the LOOP, it will --INCREMENT-- its count by --1-- every time it will encounter a --pair-- of --"unique_numbers" throughout the LOOP
        ## VERY IMPORTANT: We will use a --FLOOR DIVISION (//2)-- to find our PAIRS in "unique_numbers". It will ROUND DOWN the --RESULT-- if an --ODD number--                     e.g.: 10/2 = 5 AND 10//2 = 5; 11/2 = 5.5 AND 11//2 = 5
        total_pairs += ar.count(n) // 2
    ## Finally, we will return --"total_pairs"-- to know exactly how many pairs we have in our LIST
    return total_pairs


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()


## TEST 00
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))                                        ### ... output ... 3 (meaning 3 pairs)





### BIG O NOTATION:

### Time Complexity: O(n);
### Space Complexity: O(n).