class Timepass:
    def validParentheses(self, s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    return False
                stack.pop()


        return len(stack) == 0




s = "()()"

obj = Timepass()
print(obj.validParentheses(s))