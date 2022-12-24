<<<<<<< HEAD
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    size = len(arr)
    pos = neg = zer = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zer += 1
    pos_r = pos / size
    print('{:.6f}'.format(pos_r))
    neg_r = f'{neg / size:.6f}'
    print(neg_r)
    zer_r = zer / size
    print('{:.6f}'.format(zer_r))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
=======
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    size = len(arr)
    pos = neg = zer = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zer += 1
    pos_r = pos / size
    print('{:.6f}'.format(pos_r))
    neg_r = f'{neg / size:.6f}'
    print(neg_r)
    zer_r = zer / size
    print('{:.6f}'.format(zer_r))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
