n = int(input())
nums = [int(i) for i in input().split()]
couple = False
for i in range(n-1):
    if (nums[i]>0 and nums[i+1]>0) or (nums[i]<0 and nums[i+1]<0):
        couple = True
if couple:
    print("YES")
else:
    print("NO")