num = int(input())
i = 1
cnt = 0
while 1:
    if num > i:
        i *= 2
        cnt += 1
    else:
        print(cnt)
        break