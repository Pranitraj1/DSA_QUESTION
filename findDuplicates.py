from collections import Counter


class Timepass:
    def findDupulicates(self, nums):
        freq = {}
        result = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            if freq[num] == 2:
                result.append(num)

        return result
    def findDupulicates2(self, nums):
        result = []
        for i, num in Counter(nums).items():
            if num >=2:
                result.append(i)
        return result



nums = [1,2,3,4,4,5,6,6,7,7,8]
obj = Timepass()
print(obj.findDupulicates2(nums))