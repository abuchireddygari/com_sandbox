import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers_lkp = Counter("0123456789")
    lower_case_lkp = Counter("abcdefghijklmnopqrstuvwxyz")
    upper_case_lkp = Counter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters_lkp = Counter("!@#$%^&*()-+")
    nc=lc=uc=sc=0
    
    for c in password:
        if c in numbers_lkp and nc==0:
            nc=nc+1
        if c in lower_case_lkp and lc==0:
            lc=lc+1
        if c in upper_case_lkp and uc==0:
            uc=uc+1
        if c in special_characters_lkp and sc==0:
            sc=sc+1
    return max((nc+lc+uc+sc),6-n)
if __name__ == '__main__':
    answer = minimumNumber(1, "9")
    print(answer)
