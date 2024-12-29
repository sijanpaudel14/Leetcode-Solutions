class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mymap = {}
        start = 0
        max_len = 0
        for end in range(len(s)):   
            char = s[end]
            if char in mymap and mymap[char] >= start:
                start =mymap[char] + 1
            mymap[char] = end
            max_len = max(max_len, end-start+1)
        return max_len
