# Problem 3 : Largest prime factor

import math

def largest_prime_factor(n):
    largest = 0
    
    while n % 2 == 0:
        largest = 2
        n //= 2  
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest = i
            n //= i  
    
    if n > 2:
        largest = n
    
    return largest

print(largest_prime_factor(600851475143))
