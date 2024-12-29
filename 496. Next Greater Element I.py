class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        hashMap = {n:i for i, n in enumerate(nums1)}
        n = len(nums2)
        res = [-1] * len(nums1)
        stack = []

        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                value = nums2[stack.pop()]
                res[hashMap[value]] = nums2[i]
            if nums2[i] in hashMap:
                stack.append(i)
        return res
