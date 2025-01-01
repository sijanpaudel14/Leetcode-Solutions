class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        prev_end = float('-inf')  # End time of the last non-overlapping interval
        count = 0  # Count of intervals to remove
        
        # Iterate through intervals
        for start, end in intervals:
            if start >= prev_end:
                # No overlap, update the end of the last non-overlapping interval
                prev_end = end
            else:
                # Overlap detected, increment removal count
                count += 1
        
        return count
