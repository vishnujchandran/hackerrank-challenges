<<<<<<< HEAD
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[:-2]
    hours, minutes, seconds = time.split(":")

    if "AM" in s:
        if hours == '12':
            hours = '00'
    elif "PM" in s:
        if hours != '12':
            hours = str(int(hours) + 12)
    time = ":".join([hours, minutes, seconds])
    return time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

=======
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[:-2]
    hours, minutes, seconds = time.split(":")

    if "AM" in s:
        if hours == '12':
            hours = '00'
    elif "PM" in s:
        if hours != '12':
            hours = str(int(hours) + 12)
    time = ":".join([hours, minutes, seconds])
    return time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

>>>>>>> 12ae9d3d78172ca3677deca0f65cc9923ce987ad
