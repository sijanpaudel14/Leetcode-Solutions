#Using Min heap in python
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Min-heap of size k
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)  # Push the current number into the heap
            
            # If the heap size exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the heap is the k-th largest element
        return min_heap[0]   


