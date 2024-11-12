"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""
def longestConsecutive(nums):
    # Because the array converted into the set is outside of the actual calculation for longest, the solution still remains O(n)
    # For reference, the conversion of the array into a set is O(n) complexity
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n-1) not in numSet: # If there is not value one step below our current number, then it begins a sequence
            length = 1
            while (n + length) in numSet: # Increment until there is no value within a one step increment above
                length += 1
            longest = max(length, longest) # Check if the current set is longer than the current longest
        
    return longest
