<<<<<<< HEAD
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here

    stair = " " * n
    for i in range(n):
        print(stair[:n - i - 1] + "#" * (i + 1))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
=======
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here

    stair = " " * n
    for i in range(n):
        print(stair[:n - i - 1] + "#" * (i + 1))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
