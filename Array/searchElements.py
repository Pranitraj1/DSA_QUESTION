class Timepass:
    def Linearserch(self, nums, target):
        for i in nums:
            if i == target:
                return True
        return False





nums = [1,2,3,5,6,7,8,9]
target = 9
obj = Timepass()
print(obj.Linearserch(nums, target))