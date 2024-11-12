def isPalindrome(s):
    clean_s = ""
    
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    return new_s == new_s[::-1]