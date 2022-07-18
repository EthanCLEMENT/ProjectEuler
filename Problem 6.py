sum_of_squares = 0
square_of_sum = 0
for i in range(1,101):
    sum_of_squares += i**2

for i in range(1,101):
    square_of_sum += i

print(abs(sum_of_squares - square_of_sum**2))
