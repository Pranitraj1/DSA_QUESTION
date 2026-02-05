class Timepass:
    def missingNumber(self, arr, n):
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum

    def missingNumber2(self, arr, n):
        freq ={}
        for num in arr:
            freq[num] = 1

        for i in range(1, n+1):
            if i not in freq:
                return "this is missing number", i

arr = [1,2,4,5]
n = 5
obj = Timepass()
print(obj.missingNumber(arr, n))
print(obj.missingNumber2(arr, n))