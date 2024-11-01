

def sequencefinder(nums):
    # Because the array converted into the set is outside of the actual calculation for longest, the solution still remains O(n)
    # For reference, the conversion of the array into a set is O(n) complexity
    numSet = set(nums)
    longest = 0

    for n in nums:
        if n-1 in numSet: # If there is not value one step below our current number, then it begins a sequence
            length = 1
        while (n + length) in numSet: # Increment until there is no value within a one step increment above
            length += 1
        longest = max(length, longest) # Check if the current set is longer than the current longest
        
    return longest

    



sequencefinder([2,20,4,10,3,4,5])