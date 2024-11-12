from collections import deque

class Stack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, val):
        self.queue1.append(val)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.is_empty():
            return None
        return self.queue2.popleft()
    
    def top(self):
        if self.is_empty():
            return None
        return self.queue2[0]
    
    def is_empty(self):
        return not self.queue2