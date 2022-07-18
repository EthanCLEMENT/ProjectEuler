def Palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

i = 100
j = 100
greatest = 0
while (i <= 999):
    while (j <= 999):
        product = i * j
        if (product > greatest and Palindrome(str(product))):
            greatest = product
        j += 1
    j = 100
    i += 1
print (str(greatest))
