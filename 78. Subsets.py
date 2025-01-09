class Solution:
    def subsets(self, nums):
        # Initialize the result list to store all subsets
        result = []
        
        # Helper function to generate subsets using backtracking
        def backtrack(start, current_subset):
            """
            This helper function uses backtracking to generate all subsets.
            
            :param start: The current index from which we will include elements.
            :param current_subset: The current subset being built.
            """
            # Add the current subset to the result. Make a copy to avoid modifying it later.
            result.append(current_subset[:])  # Copy the current subset
            
            # Explore the inclusion of each element starting from the current index.
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                
                # Recursively explore subsets including nums[i]
                backtrack(i + 1, current_subset)  # Move to the next index
                
                # After recursion, backtrack by removing nums[i] from the subset
                current_subset.pop()  # Remove the last element added to current_subset
        
        # Start backtracking from index 0 and an empty subset
        backtrack(0, [])
        
        # Return the result containing all possible subsets
        return result
