class Solution:
    def majorityElement(self, nums):
        # Initialize candidate and count
        candidate = None
        count = 0
        
        # Iterate through each number in the array
        for num in nums:
            # If count is 0, pick a new candidate
            if count == 0:
                candidate = num
                count = 1  # Set count to 1 since we've found the first occurrence of the candidate
            # If the current number is the same as the candidate, increment count
            elif num == candidate:
                count += 1
            # If the current number is different, decrement count
            else:
                count -= 1
        
        # Return the candidate, which is guaranteed to be the majority element
        return candidate
    

# [3, 3, 4, 2, 4, 4, 2, 4, 4]