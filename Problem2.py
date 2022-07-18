a, b = 1, 2
ans = 0
while b <= 4000000:
    if b % 2 == 0:
        ans += b
    a, b = b, a + b
print(ans)
