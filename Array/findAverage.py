class Timepass:
    def findAverage(self, nums):
        total = 0
        n = len(nums)
        for i in nums:
            total = total + i
        return total/n



nums = [1,2,3,4,5,6,7,8,9]
obj = Timepass()
print(obj.findAverage(nums))