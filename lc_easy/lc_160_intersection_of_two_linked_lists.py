# LC 160 – Intersection of Two Linked Lists

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # Traverse until both pointers are equal (either None or intersection node)
        while pA != pB:
            # If pA reaches end, redirect to headB
            pA = pA.next if pA else headB
            # If pB reaches end, redirect to headA
            pB = pB.next if pB else headA
        
        return pA   # Either intersection node or None

