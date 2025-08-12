# LC 21 Merger two sorted list (list is linked list)

"""
Understanding the problem 

We are given heads of two sorted linked list list1 and list2 in asecnding order. We need to merger the two list into one sorted list containing all the nodes from both lists.
Rules or constraints: We need to modify the original lists instead of creating a new one. Merged list should preserve the sorted order. 
If one list become empty (or ends) before the other, then attach the rest of the remaining list as is.
If both are empty, return None.  
"""


# Brute force approach
"""
Traverse both linked lists. store all values in a normal list. Sort the list. Build a new linked list from the sorted values.
Return the heads of this new list 
"""

# Definition for singly linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


# approch BF

def mergedTwoList1(list1, list2):
    values = []

    # step 1 collect all values from list1
    while list1:
        values.append(list1.val)
        list1 = list1.next

    # Step 2 collect all values from list2
    while list2:
        values.append(list2.val)
        list2 = list2.next

    # Step 3 sort all values
    values.sort()

    # Step 4 create a new linked list from sorted values
    dummy = ListNode()
    current = dummy

    for val in values:
        current.next = ListNode(val)
        current = current.next

    # step 4 Return new list head
    return dummy.next


# test cases
# helper to create linked list from python list
def create_linked_list(lst):
    dummy =ListNode()
    current = dummy

    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# helper function to print linked list 
def linked_list_to_list(node):
    result = []

    while node: 
        result.append(node.val)
        node = node.next
    return result

# -- test cases
l1 = create_linked_list([1,2,4])
l2 = create_linked_list([1,3,4])
print("BF:", linked_list_to_list(mergedTwoList1(l1,l2))) # [1,1,2,3,4,4]

l1 = create_linked_list([])
l2 = create_linked_list([0])
print("BF:", linked_list_to_list(mergedTwoList1(l1, l2)))  # [0]

l1 = create_linked_list([5, 6, 7])
l2 = create_linked_list([1, 2, 3])
print("BF:", linked_list_to_list(mergedTwoList1(l1, l2)))  # [1, 2, 3, 5, 6, 7]

l1 = create_linked_list([])
l2 = create_linked_list([])
print("BF:", linked_list_to_list(mergedTwoList1(l1, l2)))  # []

l1 = create_linked_list([1, 2, 3])
l2 = create_linked_list([1, 1, 1])
print("BF:", linked_list_to_list(mergedTwoList1(l1, l2)))  # [1, 1, 1, 1, 2, 3]



# Optimal approach
"""
We will use the two pointer approach:
1. create a dummy node -> which acts as a starting point so we don't lose the head of the merged list.
2. Have a pointer `tail` that always points to the last node in the merged list.
3. Compare the current node of lsit1 and list2:
    append the smaller one to `tail.next`
    move that list's pointer ahead
4. Continue until one list is empty 
5. Append the remaining nodes from the non-empty list
"""

def mergedTwoList2(lst1: ListNode, lst2: ListNode):
    dummy = ListNode()
    tail = dummy

    while lst1 and lst2:
        if lst1.val < lst2.val:
            tail.next = lst1
            lst1 = lst1.next
        else:
            tail.next = lst2
            lst2 = lst2.next
        tail = tail.next
    if lst1:
        tail.next = lst1
    elif lst2:
        tail.next = lst2

    return dummy.next


# Test cases

lst1 = create_linked_list([1,2,4])
lst2 = create_linked_list([1,3,4])
print("Optimal:", linked_list_to_list(mergedTwoList2(lst1, lst2))) # [1, 1, 2, 3, 4, 4] 

lst1 = create_linked_list([])
lst2 = create_linked_list([0])
print("Optimal:", linked_list_to_list(mergedTwoList2(lst1, lst2)))  # [0]

lst1 = create_linked_list([5, 6, 7])
lst2 = create_linked_list([1, 2, 3])
print("Optimal:", linked_list_to_list(mergedTwoList2(lst1, lst2)))  # [1, 2, 3, 5, 6, 7]

lst1 = create_linked_list([])
lst2 = create_linked_list([])
print("Optimal:", linked_list_to_list(mergedTwoList2(lst1, lst2)))  # []

lst1 = create_linked_list([1, 2, 3])
lst2 = create_linked_list([1, 1, 1])
print("Optimal:", linked_list_to_list(mergedTwoList2(lst1, lst2)))  # [1, 1, 1, 1, 2, 3]
