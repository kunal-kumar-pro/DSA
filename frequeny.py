nums = [4,1,2,1,2]
nums.sort()
i = 0
while i < len(nums):
    if i == len(nums) - 1:
        print(nums[i])
        break
    if nums[i] == nums[i+1]:
        i += 2
    else:
        print(nums[i])
        break