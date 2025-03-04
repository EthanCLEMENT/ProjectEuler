# Problem 12 : Highly Divisible Triangular Number

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return len(divisors)

def triangle():
    triangle_number = 0
    i = 1
    while True:  
        triangle_number += i
        if get_divisors(triangle_number) >= 500:
            return triangle_number
        i += 1

print(triangle())