class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the current node
        self.next = next  # Pointer to the next node in the list

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Create a dummy node to simplify result handling
        dummy = ListNode()
        current = dummy  # Pointer to build the result list
        carry = 0  # Initialize carry to 0

        # Traverse both linked lists until there are no nodes left in either and no carry
        while l1 or l2 or carry:
            # Get the values of the current nodes or 0 if the node doesn't exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the values and the carry from the previous step
            total = val1 + val2 + carry
            
            # Update the carry for the next step
            carry = total // 10
            
            # Create a new node with the last digit of the total and add it to the result list
            current.next = ListNode(total % 10)
            
            # Move the current pointer forward in the result list
            current = current.next
            
            # Move to the next nodes in the input lists, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result list starting from the first node (dummy.next)
        return dummy.next
    
# Using Recursion

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the current node
        self.next = next  # Pointer to the next node

class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        # Base case: If both lists are empty and no carry, return None
        if not l1 and not l2 and carry == 0:
            return None
        
        # Get values of the current nodes, default to 0 if the node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate the sum and the new carry
        total = val1 + val2 + carry
        carry = total // 10  # Carry for the next digit
        value = total % 10   # Value to store in the current node
        
        # Create a new node with the calculated value
        result = ListNode(value)
        
        # Recursively calculate the next node
        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None
        result.next = self.addTwoNumbers(next1, next2, carry)
        
        return result
