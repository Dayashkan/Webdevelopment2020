def power(a,n):
    powerr = 1
    for i in range(0, n):
        powerr*= a
    print(powerr)

first, second = input().split()
first,second = float(first),int(second)
power(first,second)