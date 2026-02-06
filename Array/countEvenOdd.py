class Timepass:
    def coutEvenOdd(self, nums):
        even_count = 0
        odd_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count = even_count + 1

            else:
                odd_count = odd_count + 1
        return (even_count, odd_count)


nums = [1,2,3,4,5,6,7,8,9]
obj = Timepass()
print(obj.coutEvenOdd(nums))