def longest_substring(s):
    l = 0
    r = 0
    max_len = 0
    visited = set()
    substring = ""
    if len(s) == 1 or len(s) == 0:
        return len(s)
    while r < len(s):
        if s[r] in visited:
            max_len = max(max_len, len(substring))
            l += 1
            r = l
            visited = set()
            substring = ""
        else:
            visited.add(s[r])
            substring = s[l:r]
            max_len = max(max_len, len(substring))
        print(substring)
        r += 1

    return max_len

print(longest_substring("abcabcbb"))