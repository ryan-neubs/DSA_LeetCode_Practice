# O(m * n) complexity

from collections import defaultdict

class Solution:
    def groupAnagrams(strs):
        result = defaultdict(list) # Using this so that we don't have to deal with the issue of adding new values. Everything defaults to list

        for s in strs:
            count = [0] * 26 # Creates a list of 26 zeros, each indicates a letter in the alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1 # Count the letters of each word.
            result[tuple(count)].append(s) # lists cannot be keys, we use a tuple for the key instead
        return result.values()