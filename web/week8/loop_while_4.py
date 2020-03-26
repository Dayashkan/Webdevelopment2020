n = int(input())
i = 1
two_pow = 0
while i<=n:
    if i==n:
        print("YES")
        two_pow = 1
        break
    i*=2
if two_pow == 0:
    print("NO")