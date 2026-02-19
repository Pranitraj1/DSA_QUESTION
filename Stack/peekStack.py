class Timepass:
    def peekStack(self, stack):
        if len(stack) == 0:
            return -1
        return stack[-1]


stack = [1,2,3,4,5,6,7,8,9]
obi = Timepass()
print(obi.peekStack(stack))