# Problem 19 : Counting Sundays

count=0
import datetime
for y in range(1901,2001):
    for m in range(1,13):
        if datetime.date(y,m,1).weekday()==6:
            count+=1
print(count)
