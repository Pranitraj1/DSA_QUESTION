class Timepass:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        for fast in range(0,len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        for i in range(slow,len(nums)):
            nums[i] = 0
        return nums



nums = [0,1,0,3,12]
obj = Timepass()
print(obj.moveZeroes(nums))