def isValid(s):
    brackets = {'}':'{', ')':'(', ']':'['}

    stack = []
    for i in range(len(s)):
        print(stack)
        if s[i] in brackets and not stack:
            return False
        if not s[i] in brackets:
            stack.append(s[i])
        else:
            if stack[-1] == brackets[s[i]]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    
    return True


    # if the stack is empty and we have a closing bracket, return false
    # if the stack is empty and we have an open bracket or the stack has an open bracket, append to stack
    # if we have a closing bracket, and the stack has a matching open bracket, pop from stack
    # if the stack has an open bracket and we have a non matching open bracket, return false

print(isValid('({[)]}'))