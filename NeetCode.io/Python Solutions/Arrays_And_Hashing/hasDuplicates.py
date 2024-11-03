# Brute force O(n^2)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False


# O(n) Complexity
# This has O(n) complexity because looking up an element in a set has an O(1) complexity since it looks up elements directly
# def hasDuplicate(self, nums: List[int]) -> bool:
#         visited = set()
#         for num in nums:
#             if num in visited:
#                 return True
#             else:
#                 visited.add(num)
#         return False


# O(nlogn)

def hasDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False