'''
# PLUS MINUS

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example
arr = [1,1,0,-1,-1]

There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5= 0.400000, 2/5=0.400000 and 1/5 = 0.200000. Results are printed as:

0.400000
0.400000
0.200000
<p><strong>Function Description</p></strong>
Complete the plusMinus function in the editor below.</pre></code>
plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.


Input Format
The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .


Output Format
Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros

<p><strong>Sample Input</p></strong>
<pre><code>STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]</pre></code>

<p><strong>Sample Output</p></strong>
<pre><code></p></strong>0.500000
0.333333
0.166667</pre></code>
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .

'''








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
