#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    num_jumps=0
    index =0
    while index < len(c):
        if c[index] == 0:
            if index + 2 < len(c) and c[index+2] == 0 :
                num_jumps += 1
                index +=2
                continue
            if index + 1 < len(c) and c[index+1] == 0:
                num_jumps+=1
                index +=1
                continue
        index+=1
    return num_jumps
                
        
                    
                
       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
