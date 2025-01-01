class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        # Define the function to merge overlapping intervals
        def merge(intervals):
            """
            :type intervals: List[List[int]]
            :rtype: List[List[int]]
            """
            # Step 1: Sort intervals by their start value (interval[0])
            intervals = sorted(intervals, key=lambda x: x[0])
            
            # Step 2: Initialize an empty list to store the merged intervals
            merge = []
            
            # Step 3: Iterate through each interval in the sorted list
            for interval in intervals:
                # Step 4: Check if the merge list is empty or if the current interval does not overlap with the last one in merge
                if not merge or merge[-1][1] < interval[0]:
                    # No overlap, so add the current interval to the result list
                    merge.append(interval)
                else:
                    # There is overlap, so merge the current interval with the last one in merge
                    # Update the end of the last interval in merge to be the maximum of the current interval's end and the last interval's end
                    merge[-1][1] = max(interval[1], merge[-1][1])
            
            # Step 5: Return the list of merged intervals
            return merge

        # Step 6: Append the newInterval to the list of intervals
        intervals.append(newInterval)

        # Step 7: Call the merge function to merge all intervals, including the new one
        return merge(intervals)  # Return the result after merging
