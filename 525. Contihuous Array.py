class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_array = 0
        sum = 0
        myMap = {0:-1}

        for i, num in enumerate(nums):
            sum+= 1 if num ==1 else -1
            if sum in  myMap:
                l_array = max(i -myMap[sum], l_array)
            else:
                myMap[sum] = i
        return l_array