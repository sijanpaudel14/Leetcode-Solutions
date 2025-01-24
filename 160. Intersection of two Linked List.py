def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    while pA != pB:
        # Move to the next node, or switch to the other list's head
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA  # Either the intersection node or None
