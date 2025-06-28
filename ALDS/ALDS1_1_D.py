n = int(input())

max_out = float('-inf')

nums = []
for n in range(n):
    nums.append(int(input()))

min_out = nums[0]

for j in range(1,n + 1):
    max_out = max(max_out, nums[j] - min_out)
    min_out = min(min_out, nums[j]) 

print(max_out)