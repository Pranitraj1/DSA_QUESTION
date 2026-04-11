import heapq


class Solution:
    def topKFrequent(self, nums, k):

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        heap = []

        for num in freq:
            heapq.heappush(heap, (freq[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for item in heap:
            result.append(item[1])

        return result


# 🔎 Test
nums = [1, 1, 1, 2, 2, 3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))  # Output: [1,2]