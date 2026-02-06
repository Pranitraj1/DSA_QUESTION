class Timepass:
    def findminimumelement(selfs, nums):
        minimum_value = nums[0]
        for i in nums:
            if i < minimum_value:
                minimum_value = i
        return minimum_value


nums = [1,5454,6,665,56,]
obj = Timepass()
print(obj.findminimumelement(nums))