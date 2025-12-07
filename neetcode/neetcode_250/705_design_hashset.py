# LC 705 Design HashSet
"""
LC Link: https://leetcode.com/problems/design-hashset/description/
NC Link: https://neetcode.io/solutions/design-hashset

"""

# Understanding the Problem
"""
We need to create hashset class without using built in libraries. Hashset class should have 3 functions add for inserting value,  containes (checks if value is present or not)
and remove to remove value

"""

# Approach 1: Brute Force
"""
Strategy

Time Complexity:O(n)
Space Complexity:O(n)

"""

class MyHashSet:
    def __init__(self):
        self.data = []
    
    def add(self, key:int)-> None:
        if key not in self.data:
            self.data.append(key)
    
    def remove(self, key:int)-> None:
        if key in self.data:
            self.data.remove(key)
    
    def contains(self, key:int)-> bool:
        return key in self.data
    





# Approach 2: Linked List
"""
Strategy

Time Complexity
Space Complexity

"""

class ListNode:
    def __init__(self, key:int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key:int)-> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
    
    def remove(self, key:int)-> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key:int)-> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
    