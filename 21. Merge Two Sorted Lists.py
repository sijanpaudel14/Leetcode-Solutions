# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify edge case handling
        dummy = ListNode()
        current = dummy  # This will point to the last node in the merged list
        
        # Pointers to traverse both lists
        p1 = list1
        p2 = list2
        
        # Traverse both lists and merge them in sorted order
        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        # If there are any remaining nodes in either list, append them
        if p1:
            current.next = p1
        elif p2:
            current.next = p2
        
        # Return the merged list (skip the dummy node)
        return dummy.next
