# O(n) -> https://youtu.be/KLlXCFG5TnA

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevMap: # Dictionary contains values and their location key is num value, and the value is the location of that num value
                return [prevMap[diff], i]
            prevMap[n] = i