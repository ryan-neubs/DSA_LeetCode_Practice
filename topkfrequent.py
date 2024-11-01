class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {} # Create a count of each number you find
        for num in nums: 
            num_counts[num] = 1 + num_counts.get(num, 0) # Add to the count, set it equal to one if it doesn't already exist (num_counts.get(num ,0) will be 0 if the key is new)

        array = []
        for num, count in num_counts.items():
            array.append([count, num])
        array.sort() # Sort pairs of numbers and count by count. 

        result = []
        while len(result) < k:
            result.append(array.pop()[1]) # Popping will get the values in order since they are sorted

        return result