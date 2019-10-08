#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    unique_numbers = list(set(ar))
    total_pairs = 0
    for num in unique_numbers:
        total_pairs += ar.count(num) // 2
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