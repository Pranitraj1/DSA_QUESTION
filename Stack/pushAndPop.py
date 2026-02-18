class Timepass:
    def pushAndPop(self, stack, x):
        stack.append(x)
        return stack.pop()

stack = [5, 6, 7, 8, 9]
x = 10
obj = Timepass()
print(obj.pushAndPop(stack, x))