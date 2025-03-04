# Problem 4 : Largest Palindrome Product

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome():
    ans = 0
    for a in range(999, 99, -1):
        for b in range(a, 99, -1): 
            product = a * b
            if product <= ans: 
                break
            if is_palindrome(product):
                ans = product
    return ans

print(largest_palindrome())