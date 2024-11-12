def isPalindrome(s):
    clean_s = ""
    
    for char in s:
        if char.isalnum():
            clean_s += char.lower()

    return clean_s == clean_s[::-1]