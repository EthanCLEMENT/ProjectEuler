# Problem 20 : Factorial Digit Sum

import math

def main():
    factorial = math.factorial(100)
    factorial_str = str(factorial)
    ans = 0
    for i in map(int, factorial_str):
        ans += i
    return ans

print(main())
