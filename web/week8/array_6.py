n = int(input())
nums = [int(i) for i in input().split()]
cnt=0
for i in range(1,n-1):
    if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
        cnt+=1
print(cnt)