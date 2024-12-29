class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = sum(nums[:k])
        max_total = total
        
        for i in range(len(nums) - k):
            if(k>len(nums)):
                return 0
            total =total - nums[i] + nums[i+k]
            max_total = max(max_total, total)
        return float(float(max_total)/k)

