# n = 5
# prev0 = 0
# prev1 = 1
# c = 0
# for i in range(2,n+1):
#     c = prev1 + prev0
#     prev1,prev0 = c,prev1 
# print(c)

# arr = [1,2,3,4]
# print(arr[0:4])

# print(1<1)
# a = [1,22,34,25,2,24,8]
# b = a
# print(b) 

# a = {"car" : 1, "bike" : 2,}
# b = a.keys()
# b = list(b)
# print(b,type(b))
# print("car" in  a)
# unique_num = {}
# for i in nums:
#     if not(i in unique_num) :
#         unique_num[i] = 0
# nums = list(unique_num.keys())
# print(type(nums[0]))

# for i in range (len(nums)  - 1) :
#     if nums[i] == nums[i+1] :
#         nums.pop(i+1)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# i = 0 
# count = len(nums) - 1

# while i < count:  # Changed to i < count
#     if nums[i] == nums[i + 1]:
#         nums.pop(i + 1)
#         count -= 1  # Decrease count since we've removed an element
#     else:
#         i += 1  # Only move to the next element if no removal occurred

# print(nums)
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         nums[:] = nums[-k:] + nums[:-k]

#         return nums

# a = Solution()
# arr = [1,2,3,4,5,6,7,8,9,10]
# for i in range(11) :
#     b = a.rotate([1,2,3,4,5,6,7,8,9,10],i)
#     print(i,"",b)
# print(arr[-2:]+arr[:-2])

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]

        return nums

a = Solution()
arr = [1,2,3,4,5,6,7,8,9,10]
for i in range(11) :
    b = a.rotate([1,2,3,4,5,6,7,8,9,10],i)
    print(i,"",b)
print(arr[-2:]+arr[:-2])