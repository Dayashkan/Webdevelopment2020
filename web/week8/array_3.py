n = int(input())
cnt=0
nums = [int(i) for i in input().split()]
for i in nums:
    if i>0:
        cnt+=1
print(cnt)