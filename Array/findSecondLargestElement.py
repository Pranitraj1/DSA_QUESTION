class Timepass:
    def secondLargest(self, nums):
        largest = nums[0]
        second_largest = nums[0]
        for i in nums:
            if i > largest:
                second_largest = largest
                largest = i
            elif i > second_largest and i is not largest:
                second_largest = i
        return second_largest



nums =  [3, 5, 1, 9, 2]
obj = Timepass()
print(obj.secondLargest(nums))