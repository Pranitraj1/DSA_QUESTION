class Timepass:
    def findmax(self, nums):
        maximum_value = nums[0]
        for i in nums:
            if i > maximum_value:
                maximum_value = i
        return maximum_value




nums = [5664, 4656, 6566565, 665656565656,56565656565656565]
obj = Timepass()
print(obj.findmax(nums))

