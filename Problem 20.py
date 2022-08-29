import math 
n=math.factorial(100)
n=str(n)
ans=0
for i in range(len(n)):
    ans+=eval(n[i])
print(ans)
