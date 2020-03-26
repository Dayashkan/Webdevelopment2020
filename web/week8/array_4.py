n = int(input())
cnt = 0
nums = [int(i) for i in input().split()]
for i in range(1,n):
    if nums[i]>nums[i-1]:
        cnt+=1
print(cnt)