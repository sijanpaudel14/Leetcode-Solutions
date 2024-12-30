import heapq

def kSmallestPairs(nums1, nums2, k):
    # Create a min-heap
    min_heap = []
    
    # Only need to consider k elements from nums1 and nums2
    for i in range(min(k, len(nums1))):  # loop through nums1 up to k elements
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # push the first element pair (i, 0)
    
    # Result list to store the k smallest pairs
    result = []
    
    while min_heap and len(result) < k:  # While there are pairs in the heap and result list is less than k
        # Get the smallest pair (sum, index1, index2)
        pair_sum, i, j = heapq.heappop(min_heap)
        
        # Append the pair (nums1[i], nums2[j]) to the result list
        result.append([nums1[i], nums2[j]])
        
        # If there is a next element in nums2 for the current pair, push it to the heap, here j+1< len(nums) is done because last element will eventually add more sum so no necessary to perform on that last number
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
    
    return result

#Algorithm
'''  
Approach:
Min-Heap: We'll use a min-heap to always extract the pair with the smallest sum.

Tuple Format: Each element in the heap will be a tuple of the form (sum, i, j), where i is the index in nums1 and j is the index in nums2.

Initial Pairs: Start by inserting the first pair from nums1 and nums2 into the heap. The idea is to begin with pairs involving the smallest element of nums2 (i.e., nums2[0]), and then expand one pair at a time.

Expand the Pair: Once the smallest pair is extracted, if possible, insert the next possible pair by advancing the index of nums2 (i.e., move from nums2[j] to nums2[j+1]).

Termination: The process continues until we've found k pairs or exhausted the possibilities.


Let's say nums1 = [1,7,11] and nums2 = [2,4,6], and we want to find k = 3 smallest pairs:

Step 1: Initialize the heap with the first pair combinations involving nums2[0]:

heap = [(1+2, 0, 0), (7+2, 1, 0), (11+2, 2, 0)]
Heap contents: [(3, 0, 0), (9, 1, 0), (13, 2, 0)]
Step 2: Extract the smallest pair (3, 0, 0), which corresponds to [1, 2].

Add the next pair: (1 + 4, 0, 1) → heap = [(5, 0, 1), (9, 1, 0), (13, 2, 0)]
Result: [[1, 2]]
Step 3: Extract the next smallest pair (5, 0, 1), which corresponds to [1, 4].

Add the next pair: (1 + 6, 0, 2) → heap = [(7, 0, 2), (9, 1, 0), (13, 2, 0)]
Result: [[1, 2], [1, 4]]
Step 4: Extract the next smallest pair (7, 0, 2), which corresponds to [1, 6].

Result: [[1, 2], [1, 4], [1, 6]]


'''

