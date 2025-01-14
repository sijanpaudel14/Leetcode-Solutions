class Solution(object):
    def isValid(self, s):
        # Define the hashmap with closing brackets as keys and opening brackets as values
        hashmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Initialize an empty stack to store opening brackets
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in hashmap.values():  # Opening brackets are in hashmap values
                stack.append(char)
            # If the character is a closing bracket, check if it matches the last opening bracket
            elif char in hashmap:  # Closing brackets are in hashmap keys
                # If stack is empty or the last opening bracket doesn't match, return False
                if not stack or stack[-1] != hashmap[char]:
                    return False
                # Otherwise, pop the last opening bracket from the stack
                stack.pop()
        
        # If the stack is empty, return True (balanced), otherwise False (unbalanced)
        return not stack