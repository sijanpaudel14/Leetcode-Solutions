import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each element
        freq_map = Counter(nums)
        
        # Step 2: Use a min-heap to keep the top k frequent elements
        min_heap = []
        
        # Step 3: Push the frequency and number as tuples into the heap
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            
            # If the heap size exceeds k, remove the smallest frequency element
            if len(min_heap) > k:
                heapq.heappop(min_heap) 
        
        # Step 4: Return only the numbers (second part of each tuple in the heap)
        return [num for freq, num in min_heap]