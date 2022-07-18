def isPrime(x):
    if x <= 1:
        return False

    for i in range(2,x):
        if x % i == 0:
            return False 
      
    return True

number = 600851475143 
factors = []
factors.append(1)

for i in range(2, number//2 + 1):
    if number % i == 0:
        if isPrime(i) == True:
            factors.append(i)

print(max(factors))
