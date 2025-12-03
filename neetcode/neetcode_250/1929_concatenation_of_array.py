# LC_1929 Concatenation of Array
'''
LC Link: https://leetcode.com/problems/concatenation-of-array/description/
NC Link: https://neetcode.io/solutions/concatenation-of-array

'''
# Understanding problem
'''
Take a list and produce a new list that repeats it twice.

Its important for interview whether its creating new list or in-place modification
- creates new list -> returns new list, original unchanges
- in place modification -> modifies original list directly (interviwer twist)
'''


# Approach 1: List Multiplication
'''
Strategy: Using python inbuilt function -- multiplication orperator (*). create a new list with `nums * 2`(if 3 times then * 3, pythonic solution)
List behaviour: creates new list - original input 'nums' remains unchanged - not in place modification, memory: original (n elements) + Result (2n elements)

Time Complexity: O(n) - creates 2n elements
Space Complexity: O(n) - for the output array (input not counted)

Pros: single line solution, readable, pythonic, optimal performance, safe - prevents original data
Cons: if interviewer ask for inplace this wont work, uses extra space for new list

Interview tip: if asked "can yoou do this inplace? use Approach 3 extend one instead



'''

def getConcatenation_multi(nums):
    return nums * 2

# Approach 2: List Addition
'''
Strategy: Use + operator to concatenate two lists (nums + nums) - equally good as multiplication approach.
List behaviour: create new list - original remains unchanged - returns new list - not in place modification - memory: original (n elements) + Result (2n elements)

Time complexity: O(n)
Space Complexity: O(n)

Pros: Clean and simple, readable, optimal, create new list
Cons: if interviewer ask for inplace this wont work, uses extra space for new list

Interview tip: if asked "can yoou do this inplace? use Approach 3 extend one instead

'''

def getConcatenation_add(nums):
    return nums + nums

# Approach 3: Using .extend()
'''
Strategy: use .extend() to add elements in place - must use nums.copy() or num[:] to avoid infinite loop - modifies the original list directly

List behavious: In place modification - original list direclty modified, no new list (same object), result is stored in same memory location, memory: original list grows from n to 2n elements

Time Complexity: O(n)
Space Complexity: O(n) - creates temporary copy for extension only

Pros: In place modification - saves space, Works when interviewer requires modifying input, only one list object in memory, good for constrained memory scenarios
Cons: Modifies input (destructive operations), less readable, must remember to retrun lsit, still create temporary copy inrerally for nums[:]

Interview tip: use this if asked can you do in place. 


'''

def getConcatenation_extend(nums):
    nums.extend(nums[:]) # .copy() or or nums[:] to prevent infinite loop 
    return nums # returns modifed list

# Approach 4: For loop with copy - inplace
'''
Streagey: iterate over a copy of the array, append each element to the original array, demonstrate why .copy() is needed in loops
List behviour: Inplace modification, original input 'nums' is modified, creates temp copy only for iteration, final result stored in original list

Time Complexity: O(n)
Space Complexity: O(n) - temporary copy for safe iteration

Pros: shows iteration concetp, works correctly, in-place
Cons: verbose (3 lines vs 1)


'''

def getConcatenation_fl(nums):
    for i in nums.copy(): #must uss ,copy() or nums[:] to avoid infinite loop
        nums.append(i)
    return nums

# Approach 5: Manual index manipulation
'''
Streategy: pre allocate aarray of size 2n, use index arithmetic to place elements, most explicit approach
List behvior: creates new list of size 2n, original unchanged, pre allocates memory for efficency

Time Complexity: O(n)
Space Complexity: O(n)

Pros: shows index manipulation, similar to other languages (C++ and java), pre-allocation can be effient, doesn't modify input
Cons: verbose and unnecessary in python, less pythonic, not in place

Interview tip:
good for demonstrating algorithm understanding


'''
def getConcatenation_manual(nums):
    n = len(nums) # store the length of the list, done to know how many elements to copy and determine where the second half starts
    ans = [0] * (2*n) # pre-allocate space - create a new list of size 2n filled with zero, zero is placeholder values we will overwrite every element later, this is efficient because python doesn't need to resize the list repeatedly
    for i in range(n): # runs loop from index 0 to index n-1
        ans[i]=nums[i] # will copy nums[i] into two places inside ans
        ans[i+n] = nums[i] # copy nums[i] to second half of ans, at one time its updating 2 elements at 0th index and 3 index and so on
    return ans


# Approach 6 :Neetcode approach (iteration - two pass)

def getConcatenation_nc(nums):
    ans = [] # empty list (dynammic growth)
    for i in range(2): # 2 iternations ** can be made 3 or 4
        for num in nums: # n iterations each
            ans.append(num) # O(1) operation
    return ans

# Test Cases

import unittest

class TestConcatenation(unittest.TestCase):
    # helper to resue expected result
    def assertConcatenation_new_list(self, func, nums):
        original = nums[:]
        result = func(nums)
        expected = original * 2
    
        # Correctness
        self.assertEqual(result, expected)

        # Original should not be modified
        self.assertEqual(nums, original)
    
    def assertConcatenation_in_place(self, func, nums):
        original = nums[:] # copy for expected calculation
        result = func(nums)
        expected = original * 2

        # correctness: function should return the modified list
        self.assertEqual(result, expected)

        # Original must be modified in place
        self.assertEqual(nums, expected)

    # Test for new list approaches
    def test_multi(self):
        nums = [1,2,1]
        self.assertConcatenation_new_list(getConcatenation_multi, nums)

    def test_add(self):
        nums = [1,2,1]
        self.assertConcatenation_new_list(getConcatenation_add, nums)

    def test_manual(self):
        nums = [1,2,1]
        self.assertConcatenation_new_list(getConcatenation_manual, nums)

    def test_neetcode(self):
        nums = [1,2,1]
        self.assertConcatenation_new_list(getConcatenation_nc, nums)
    

    # Test for in place approaches
    def test_extend(self):
        nums = [1,2,1]
        self.assertConcatenation_in_place(getConcatenation_extend, nums)
    
    def test_forloop(self):
        nums = [1,2,1]
        self.assertConcatenation_in_place(getConcatenation_fl, nums)

    # Edge Cases
    def test_empty_list(self):
        nums = []

        # new list approaches
        self.assertConcatenation_new_list(getConcatenation_multi, nums[:])
        self.assertConcatenation_new_list(getConcatenation_add, nums[:])
        self.assertConcatenation_new_list(getConcatenation_manual, nums[:])
        self.assertConcatenation_new_list(getConcatenation_nc, nums[:])
        
        # inplace approaches
        self.assertConcatenation_in_place(getConcatenation_extend, nums[:])
        self.assertConcatenation_in_place(getConcatenation_fl, nums[:])

    def test_single_element(self):
        nums = [5]
        self.assertConcatenation_new_list(getConcatenation_multi, nums[:])
        self.assertConcatenation_new_list(getConcatenation_add, nums[:])
        self.assertConcatenation_new_list(getConcatenation_manual, nums[:])
        self.assertConcatenation_new_list(getConcatenation_nc, nums[:])
        self.assertConcatenation_in_place(getConcatenation_extend, nums[:])
        self.assertConcatenation_in_place(getConcatenation_fl, nums[:])

    def test_negative_and_zero(self):
        nums = [0, -1, 2]
        self.assertConcatenation_new_list(getConcatenation_multi, nums[:])
        self.assertConcatenation_new_list(getConcatenation_add, nums[:])
        self.assertConcatenation_new_list(getConcatenation_manual, nums[:])
        self.assertConcatenation_new_list(getConcatenation_nc, nums[:])
        self.assertConcatenation_in_place(getConcatenation_extend, nums[:])
        self.assertConcatenation_in_place(getConcatenation_fl, nums[:])
    
if __name__ == "__main__":
    unittest.main()






""" # using .copy() but this is not efficient as it will create 2 more list 
nums = [1,2,1]
num1 = nums.copy()
print(num1)
nums = nums + num1

print("array using copy() and concatenatetion- creates a new list :", nums)

# using .extend() --- its in place and no new list is created - most efficient i think
num = [1,2,1]
num.extend(num) # or can use .extend(num.copy()) to prevent infinite loop
print("num using .extend() in place : ",num)

# using for loop - creates a copy list--still not able to understand
arr = [1,2,1]

for i in arr.copy():
    arr.append(i)

print("array using for loop:", arr)

# using + operator, but creates a new list
nums1 = [3,4,3]
nums1 = nums1 + nums1
print("Concatenating (creates new list):", nums1)

# using simple * most suitable
arr2 = [3,4,3]
arr2 = arr2 * 2
print(arr2)
"""
