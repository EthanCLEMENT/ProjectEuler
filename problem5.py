# Problem 5 : Smallest Multiple

def smallest_positive_number():
    n = 20
    while True:
        if n % 1 == 0 and n % 2 == 0 and n % 3 == 0 and n % 4 == 0 and n % 5 == 0 and n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 10 == 0 and n % 11 == 0 and n % 12 == 0 and n % 13 == 0 and n % 14 == 0 and n % 15 == 0 and n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0 and n % 20 == 0:
            return n
        else: 
            n += 1

print(smallest_positive_number())

import math
from functools import reduce

def smallest_positive_number():
    return reduce(math.lcm, range(1, 21))

print(smallest_positive_number())
