fib = [0,1]
i = 2
while True:
	fibAdd=fib[i-1]+fib[i-2]
	fib.append(fibAdd)
	if fibAdd>10**999:
		print(i)
		break
	i = i+1
