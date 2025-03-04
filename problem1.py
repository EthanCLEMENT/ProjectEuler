# Problem 1 : Multiples of 3 or 5

def find_sum():
    ans = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans

print(find_sum())