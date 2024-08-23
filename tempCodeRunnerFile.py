i = 0 
count = len(nums) - 1

while i < count:  # Changed to i < count
    if nums[i] == nums[i + 1]:
        nums.pop(i + 1)
        count -= 1  # Decrease count since we've removed an element
    else:
        i += 1  # Only move to the next element if no removal occurred

print(nums)