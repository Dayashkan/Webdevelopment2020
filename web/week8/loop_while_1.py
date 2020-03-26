import math
n = int(input())
i = 1
while i<=n:
    sqrt = math.sqrt(i)
    if sqrt%1==0:
        print(i)
    i+=1
    