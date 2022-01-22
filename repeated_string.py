#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):

    qt_total_a = 0
    
    str_len = len(s)

    qt_a_in_s = 0 
    for i in range(0, str_len):
        if s[i] == 'a':
            qt_a_in_s+=1
    
    qt_rept = n // str_len

    qt_total_a = qt_rept * qt_a_in_s

    for i in range(0, n % str_len):
        if s[i] == 'a':
            qt_total_a +=1
    return qt_total_a
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
