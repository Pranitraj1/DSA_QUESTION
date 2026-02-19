class Timepass:
    def reverseStack(self, stack):
        temp_stack = []

        while stack:
            temp_stack.append(stack.pop())

        return temp_stack

stack = [4, 7, 9, 1]
obj = Timepass()
print(obj.reverseStack(stack))
