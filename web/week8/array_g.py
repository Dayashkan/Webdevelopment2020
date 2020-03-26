n = int(input())
nums = [int(i) for i in input().split()]
for i in range(n-1, -1, -1):
    print(nums[i], end=" ")