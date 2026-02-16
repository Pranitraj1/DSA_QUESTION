class Timepass:
    def countPosNegZero(self, nums):
        positive_count = 0
        negative_count = 0
        zero_count = 0
        for i in nums:
            if i > 0:
                positive_count = positive_count + 1
            elif i < 0:
                negative_count = negative_count + 1
            else:
                zero_count = zero_count + 1

        return (positive_count, negative_count, zero_count)


nums = [1, -2, 0, 4, -5]
obj = Timepass()
print(obj.countPosNegZero(nums))