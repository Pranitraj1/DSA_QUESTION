class Timepass:
    def reverseString(self, s):
        stack = []

        # Push all characters into stack
        for ch in s:
            stack.append(ch)

        # Pop all characters to form reversed string
        reversed_s = ''
        while stack:
            reversed_s += stack.pop()

        return reversed_s

s = "hello"
obj = Timepass()
print(obj.reverseString(s))