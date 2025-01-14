class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Sort the list in alphabetical order to bring the most different strings to the ends
        strs.sort()
        
        # Compare the first and the last string
        first = strs[0]
        last = strs[-1]
        
        # Find the longest common prefix between the first and last string
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        # The common prefix is the substring from the start to index i
        return first[:i]
