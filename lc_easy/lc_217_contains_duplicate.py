# LC 217 Contain Duplicate

"""
Understanding the problem:

Given an integer array called nums. Need to check if any number is duplicate i.e appears more than
once in array. If found then return True (there are duplicates) else return false (no duplicates)

"""

""""
Approach: Brute Forece
using len() and set() and comparing if len of array is equal to len of set array

"""

def containsDuplicateBF(nums):
    return len(nums) != len(set(nums))


# Test
print("Burte Force") 
print(containsDuplicateBF([1, 2, 3, 1]))   # True
print(containsDuplicateBF([1, 2, 3, 4]))   # False
print(containsDuplicateBF([1, 1, 1, 1]))   # True
print(containsDuplicateBF([]))             # False
print(containsDuplicateBF([99]))           # False


"""
Approach 2: using set() to store unique values

We will create an empty set that will store unique values. and then we iterate over nums and
use conditional statements to check if the number already exists in the set. If yes, duplicate 
found return True else retrun False add it to set and continue

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicateS(nums):
    seen = set() # to store unique elements

    for i in nums:
        if i in seen:
            return True # duplicate found
        seen.add(i) # store the element
    return False # no duplicates found


# Test
print("Optimal") 
print(containsDuplicateS([1, 2, 3, 1]))   # True
print(containsDuplicateS([1, 2, 3, 4]))   # False
print(containsDuplicateS([1, 1, 1, 1]))   # True
print(containsDuplicateS([]))             # False
print(containsDuplicateS([99]))           # False