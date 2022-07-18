def is_prime(nb):
    if nb == 1:
        return False
    if nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True
nb_prime = 1
i = 1
while nb_prime != 10001:
    i += 2
    if is_prime(i):
        nb_prime += 1
print(i)
