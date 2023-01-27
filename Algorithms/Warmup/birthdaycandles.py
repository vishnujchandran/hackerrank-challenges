'''
# BIRTHDAY CAKE CANDLES

You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
Example
  candles = [4,4,1,3]

The maximum height candles are 4 units high. There are 2 of them, so return 2.

<p>Function Description</p>

Complete the function birthdayCakeCandles in the editor below.
birthdayCakeCandles has the following parameter(s):
int candles[n]: the candle heights
Returns
int: the number of candles that are tallest

Input Format
The first line contains a single integer,n , the size of cabdles[].
The second line contains  space-separated integers, where each integer i describes the height of .

Sample Input 0
<pre><code>4
3 2 1 3</pre></code>
Sample Output 0
<pre><code>2</pre></code>

Explanation 0

Candle heights are . The tallest candles are  units, and there are  of them.


'''











#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    return(candles.count(max(candles)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

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
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    return(candles.count(max(candles)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
