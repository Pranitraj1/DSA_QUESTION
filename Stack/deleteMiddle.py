class Timepass:
    def deleteMiddle(self, stack):
        n = len(stack)
        mid = n//2
        temp = []


        for _ in range(mid):
            temp.append(stack.pop())

        stack.pop() #Delete the middle elements form the stack

        while temp:
            stack.append(temp.pop())

        return stack


stack = [1,2,3,4,5]
obj = Timepass()
print(obj.deleteMiddle(stack))