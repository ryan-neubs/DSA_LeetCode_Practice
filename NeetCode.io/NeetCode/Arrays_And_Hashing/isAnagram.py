# Anagrams are words that contain the exact same characters
# Our solution, check if they are equal length, else sort the letters and compare

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)