# LC 206 Reverse Linked List


class ListNode:
def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
    def reverseList (self, head: ListNode) -> ListNode:
        # recursive: T O(n), M O(n)
        if not head:
            return None
        
        newHead = head
        if head.next:
            self.reverseList(head.next)
            head.next.next = head # reversing the link
        head.next = None

        return newHead