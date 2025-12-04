# LC_217 Contain Duplicate
"""
LC Link: https://leetcode.com/problems/contains-duplicate/description/
NC Link: https://neetcode.io/solutions/contains-duplicate
"""



# Understanding problem:
"""
We need to check if any number appears more than once in an array. Return True → if there are duplicates. Return False → if all elements are unique.

Key point for interview: 'set' helps check uniqueness efficiently.

"""


# Approach 1: Using Set (Pythonic and Optimal) - Brute Forece
"""
Strategy: convert list to set, if duplicate exist, set length < list length, otherwise all unique - length equal
List behaviour: create new set object, original list remains unchanged

Time complexity: O(n)- single pass to convert to set
Space Complexity: O(n) - storing unique elements in a set
Pros:
Cons:
"""

def containsDuplicateBF(nums):
    return len(nums) != len(set(nums))


# Approach 2: Using manual Set check
"""
Strategy: Iterate over list and maintain a set of seen elements. if elements repeats return True

Time Complexity: O(n)
Space Complexity: O(n)

Pros:
Cons:

"""

def containsDuplicateS(nums):
    seen = set() # to store unique elements

    for i in nums:
        if i in seen:
            return True # duplicate found
        seen.add(i) # store the element
    return False # no duplicates found


# Test cases
import unittest

class TestContainsDuplicates(unittest.TestCase):

    def test_duplicate_present(self):
        nums = [1,2,3,1]
        self.assertTrue(containsDuplicateBF(nums))
        self.assertTrue(containsDuplicateS(nums))

    def test_no_duplicates(self):
        nums = [1,2,3,4]
        self.assertFalse(containsDuplicateBF(nums))
        self.assertFalse(containsDuplicateS(nums))
    
    def test_all_duplicates(self):
        nums = [5,5,5,5]
        self.assertTrue(containsDuplicateBF(nums))
        self.assertTrue(containsDuplicateS(nums))
    
    def test_empty_list(self):
        nums = []
        self.assertFalse(containsDuplicateBF(nums))
        self.assertFalse(containsDuplicateS(nums))
    
    def test_single_element(self):
        nums = [10]
        self.assertFalse(containsDuplicateBF(nums))
        self.assertFalse(containsDuplicateS(nums))

if __name__ == "__main__":
    unittest.main()

