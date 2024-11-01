def isPalindrome(s):
    reverse_seq = s[::-1]
    new_rev_sequence = ""
    cleaned_sequence = ""
    
    for char1, char2 in zip(s, reverse_seq):

        if char1.isalpha() or char1.isnumeric():
            cleaned_sequence += char1.lower()

        if char2.isalpha() or char2.isnumeric():
            new_rev_sequence += char2.lower()

    return new_rev_sequence == cleaned_sequence