c = 0
b = 0
a = 1000 - c - b
while a + b + c != 1000 or a**2 + b**2 != c**2:
    if a > b or b == 2:
        c += 1
        b = c - 1
    b -= 1
    a = 1000 - c - b
print(a*b*c)
