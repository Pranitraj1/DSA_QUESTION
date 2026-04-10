import heapq
class Timepass:
    def findKthLargest(self, nums, k):

        heap = []


        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


nums = [3,2,3,1,2,4,5,5,6]
k= 4
obj = Timepass()
print(obj.findKthLargest(nums, k))