# Problem 10 : Summation of Primes

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum():
    ans = 0
    for num in range(2, 2000000):
        if is_prime(num):
            ans += num
    return ans

print(sum())


