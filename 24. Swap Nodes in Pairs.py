# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)

        prev, curr = dummy, head

        while curr and curr.next:
            #save pointers for another iteration
            next = curr.next.next
            second = curr.next

            #reverse the pair
            second.next = curr
            curr.next = next

            #update the head 
            prev.next = second

            prev = curr
            curr = next

        return dummy.next

            #update pointers
            



        