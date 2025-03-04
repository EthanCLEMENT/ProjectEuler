# Problem 2 : Even Fibonacci Numbers

def find_sum(n):
    a, b = 1, 2  
    even_sum = 0

    while a <= n:
        if a % 2 == 0:
            even_sum += a
        
        a, b = b, a + b  

    return even_sum


print(find_sum(4000000))