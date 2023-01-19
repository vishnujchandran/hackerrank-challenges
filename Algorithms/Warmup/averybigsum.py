'''# A VERY BIG SUM

<p>In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.</p>

<p><strong>Function Description</p></strong>
Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .

<p><strong>Return<p></strong>
long: the sum of all array elements
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

<p><strong>Output Format</p></strong>
Return the integer sum of the elements in the array.</p></strong>


<p><strong>Sample Input<p><strong>
<pre><code>5
1000000001 1000000002 1000000003 1000000004 1000000005</pre></code>

<p><strong>Output<p><strong>
<pre><code>5000000015</pre></code>
'''













#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for x in ar: sum += x
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

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
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for x in ar: sum += x
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
