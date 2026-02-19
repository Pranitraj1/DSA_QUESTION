class Mystack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


s = Mystack()
s.push(10)
s.push(10)
print(s.peek())
print(s.pop())
print(s.isEmpty())