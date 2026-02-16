class Timepass:
    def copyArray(self,nums):
        copied_array = []
        for i in nums:
            copied_array.append(i)
        return copied_array


nums = [1, 2, 3, 4, 5]
obj = Timepass()
print(obj.copyArray(nums))