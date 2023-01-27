# SIMPLE ARRAY SUM

Given an array of integers, find the sum of its elements.
For example, if the array ,ar = [1,2,3],  1+2+3 = 6 , so return 6.

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
simpleArraySum has the following parameter(s):
ar: an array of integers

Input Format
The first line contains an integer,n , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.


Output Format
Print the sum of the array's elements as a single integer.
Sample Input
<pre><code>6

1 2 3 4 10 11</pre></code>
Sample Output
<pre><code>31</pre></code>
Explanation

We print the sum of the array's elements: 
1+2+3+4+10+11 = 31
'''

'''<<<<<<< HEAD










#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    sum = 0
    for i in ar:
        sum += i

    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
=======
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    sum = 0
    for i in ar:
        sum += i

    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
