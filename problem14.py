# Problem 14 : Longest Collatz Sequence

def longest_chain():
    ans = 1
    for n in range(1000000, 0, -1):
        count = 0
        num = n
        while num != 1:
            if num % 2 == 0:
                num //= 2  
            else:
                num = 3 * num + 1
            count += 1
        if count > ans:
            ans = count
            longest_start = n  
    return longest_start

print(longest_chain())
