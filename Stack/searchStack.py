class Timepass:
    def searchStack(self, stack, x):
        return x in stack


stack = [4, 7, 1, 9]
x = 7

obj = Timepass()
print(obj.searchStack(stack, x))