n = int(input())
nums = [int(i) for i in input().split()]
for i in range(n):
    if nums[i]%2==0:
        print(nums[i],end=' ')