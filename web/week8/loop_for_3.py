import math
a = int(input())
b = int(input())
if a < b:
 for i in range (a, b+1):
    sqrt = math.sqrt(i)
    if sqrt%1==0:
        print(i)