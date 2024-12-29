class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x  
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
