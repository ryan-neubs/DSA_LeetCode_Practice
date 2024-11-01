# THIS IS WRONG BECAUSE IT CAN ONLY SOLVE IT WITH WORDS THAT ARE LESS THAN 10 LETTERS

# def encode(strs):
#     encoded = ""
#     for string in strs:
#         encoded += str(len(string)) + ':' + string

#     return encoded

# def decode(s):
#     decoded = []
#     while s != "":
#         print(decoded)
#         decoded.append(s[1:int(s[0])+1])
#         s = s[int(s[0])+1:]
#     return decoded

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + ":" + string

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            length  = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j

        return decoded