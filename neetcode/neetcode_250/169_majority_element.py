# LC 169 Majority Element

"""
LC Link: https://leetcode.com/problems/majority-element/
NC Link:
"""
# Understanding problem
"""
We need to find the element that appears more than ⌊n/2⌋ times in an array. The problem guarantees that a majority element always exists.

Key point for interview: The majority element appears MORE than half the time, so it will always dominate any other element in frequency.
"""

# Approach 1: Frequency Count using Dictionary
"""
Strategy: Use a hash map (dictionary) to count occurrences of each element.
Then find the element with maximum frequency.

Time Complexity: O(n) - single pass to count + O(n) to find max
Space Complexity: O(n) - dictionary stores up to n unique elements

Pros: Straightforward, easy to understand, works for variations (like finding all elements > n/3)
Cons: Uses extra space, not optimal for this specific problem
"""

def majorityElement(nums):
    count = {} # dictionary to store frequency

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    # Find the key with the maximum frequency
    majority = max(count,key = count.get)

    return majority

# Approach 2: Optimal & pythonic way to do the same thing
"""
Strategy: Use dictionary's get() method with default value to simplify counting.
get(num, 0) returns 0 if key doesn't exist, otherwise returns current count.

Time Complexity: O(n) - single pass to count + O(n) to find max
Space Complexity: O(n) - dictionary stores up to n unique elements

Pros: Cleaner, more Pythonic code
Cons: Same space complexity as Approach 1 

"""

def majorityElement1(nums):
    count = {} # dictionary to store frequency 

    for num in nums:
        count[num] = count.get(num,0) + 1 # Add 1 to the current count

    #find the key with maximum value
    return max(count, key = count.get)


import unittest

class TestMajorityElement(unittest.TestCase):
    
    def test_simple_majority(self):
        nums = [3, 2, 3]
        self.assertEqual(majorityElement(nums), 3)
        self.assertEqual(majorityElement1(nums), 3)
    
    def test_longer_array(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(majorityElement(nums), 2)
        self.assertEqual(majorityElement1(nums), 2)
    
    def test_single_element(self):
        nums = [1]
        self.assertEqual(majorityElement(nums), 1)
        self.assertEqual(majorityElement1(nums), 1)
    
    def test_all_same(self):
        nums = [5, 5, 5, 5, 5]
        self.assertEqual(majorityElement(nums), 5)
        self.assertEqual(majorityElement1(nums), 5)
    
    def test_barely_majority(self):
        nums = [1, 1, 2, 2, 1]
        self.assertEqual(majorityElement(nums), 1)
        self.assertEqual(majorityElement1(nums), 1)

if __name__ == "__main__":
    unittest.main()