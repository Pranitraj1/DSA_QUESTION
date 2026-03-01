class Timepass:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left = left + 1
            right = right - 1
        return s

s = ["p", "r", "a" , "n", "i", "t"]
obj = Timepass()
print(obj.reverseString(s))
