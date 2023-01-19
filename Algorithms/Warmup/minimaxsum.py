'''
# MINI-MAX SUM
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Example
arr = [1,3,,5,7,9]
The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 =24 . 
The function prints
16 24

<p>Function Description<p>

Complete the miniMaxSum function in the editor below.
miniMaxSum has the following parameter(s):
arr: an array of 5 integers
Print
Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

Input Format

A single line of five space-separated integers.

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input
<pre><code>1 2 3 4 5</pre></code>
Sample Output
<pre><code>10 14</pre></code>
Explanation

The numbers are 1, 2, 3, 4 and 5. Calculate the following sums using four of the five integers:

Sum everything except , the sum is 2+3+4+5 =14.
Sum everything except , the sum is 1+3+4+5 =13.
Sum everything except , the sum is 1+2+4+5 =12.
Sum everything except , the sum is 1+2+3+5 =11.
Sum everything except , the sum is 1+2+3+4 =10.

'''<<<<<<< HEAD












#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total = sum(arr)
    mini = total - max(arr)
    maxi = total - min(arr)
    print(mini, maxi)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
=======
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total = sum(arr)
    mini = total - max(arr)
    maxi = total - min(arr)
    print(mini, maxi)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
