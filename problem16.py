# Problem 16 : Power Digit Sum

def sum_of_digits(n):
    num = 2**n
    num_str = str(num)
    ans = 0
    for i in map(int, num_str):
        ans += i
    return ans

print(sum_of_digits(1000))