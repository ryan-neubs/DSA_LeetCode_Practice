class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self):
        self.minstack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]