def evalRPN(tokens):
    operation_stack = []
    for token in tokens:
        operation_stack.append(token)
        if operation_stack[-1] == '+':
            operation_stack.pop()
            operation_stack.append(int(operation_stack.pop()) + int(operation_stack.pop()))
        if operation_stack[-1] == '-':
            operation_stack.pop()
            operation_stack.append(int(operation_stack.pop()) - int(operation_stack.pop()))
        if operation_stack[-1] == '*':
            operation_stack.pop()
            operation_stack.append(int(operation_stack.pop()) * int(operation_stack.pop()))
        if operation_stack[-1] == '/':
            operation_stack.pop()
            operation_stack.append(int(operation_stack.pop()) / int(operation_stack.pop()))

    return int(operation_stack[0])

print(evalRPN(["2","1","+","3","*"]))