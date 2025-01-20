class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If the list is empty or has only one node, return it as is
        if not head or not head.next:
            return head

        # Initialize the current pointer to the head of the list
        current = head

        # Traverse the linked list
        while current and current.next:
            # If the current node's value is equal to the next node's value
            if current.val == current.next.val:
                # Skip the next node by updating the next pointer
                current.next = current.next.next
            else:
                # Move to the next node only if no duplicate was found
                current = current.next

        return head
