# Anagrams are words that contain the exact same characters
# Solution: Creates an array of 26 0s signifyng each char of alphabet. 
# - if s has an 'a' we add 1 to the first position in the array
# - if t has an 'a' we subtract 1 in the first position meaning both strings contain it
# - therefore, if s and t have the same letters the array will just be 0s

class Solution:
    def isAnagram(s, t) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26 # Create array of length 26 for each letter of alphabet
        for i in range(len(s)): 
            count[ord(s[i]) - ord('a')] += 1 # Calculate position of current letter
            count[ord(t[i]) - ord('a')] -= 1 # If both strings contain that letter they will cancel each other out

        for val in count:
            if val != 0: # We want count to be all 0s which will signify an anagram
                return False
        return True