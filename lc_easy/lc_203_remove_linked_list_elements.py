# LC 203 Remove linked list elements
"""
Linked list

its a linear data structure that stores a sequence of elements (nodes) where each element contains data and a pointer (reference) to
the next element in the list. Unlike arrays, linked lists do not store elements in contiguous memory locations.

Key concepts
1. Nodes: Each element in a linked list is called a node. A node typically contains two parts
    - Data: the actual value being stored in the node
    - Pointer (reference/link): A pointer to the next node in the sequence. This pointer is what links the nodes together.
2. Head: first node in the list is called the head
3. Tail: last node in the list points to `null` or `None`, indicating the end of the list.
4. Singly Linked List: Each node has a pointer to the next node only
5. Doubly Linked List: Each node has pointer to both the next and the previous node. allows navigation both forward and backward.
6. Circular Linked List: forms a loop and connects the last node back to the first node, which is great for circular queues or buffering.


How it works
1. Data storage: Nodes can be stored anywhere in memory, not necessarily in contiguous location.
2. Traversal: To access a specific element in a linked list, we must start at the head and follow the pointers from one node to the next untill you reach the desired element.
3. Dynamic Size: Linked Lists can easily grow or shrink in size as needed, unlike arrays which may have been fized size.

"""


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def removeElements(self, head:ListNode, val: int)-> ListNode:
        dummy = ListNode(next = head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next

            if curr.val == val: # delete curr by skipping it
                prev.next = nxt 
            else:               # keep curr and move prev
                prev = curr
            curr = nxt          # always advance curr
        return dummy.next
    

# Building list manually
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

sol = Solution()
new_head = sol.removeElements(head, 6)

# Traverse and print
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 3 -> 4 -> 5 ->
