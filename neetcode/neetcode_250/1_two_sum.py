# LC_1 two sum
"""
LC Link: https://leetcode.com/problems/two-sum/description/
NC Link: https://neetcode.io/solutions/two-sum
"""

# Understanding the problem
"""
With a list of numbers and a target value. Task is to find two different numbers in the list that add up to the target 
and return their index positions. The input always has exactly one valid answer.

"""

# Approach 1: Using for loop (brute force)
'''
Strategy: Compare every possible pair using two loops.
Time Complexity: O(n^2)
Space Complexity: O(1)

'''
def twoSumL(nums, target):
    for i in range(len(nums)): 
        for j in range(i + 1, len(nums)): 
            if nums[i] + nums[j] == target: 
                return [i, j] 


# Using Dictionary and finding only differnce 
'''
Strategy: Use a dictionary to store numbers and their indices as we iterate.
For every number, check if (target - num) exists in the dictionary. If yes → found the pair.
Time Complexity: O(n) 
Space Complexity: O(n)

'''

def twoSumD(nums: list, target: int):
    prevMap = {} #empty dict which will store nos or elements as key and index as values

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[num] = i



# Test cases
import unittest

class TestTwoSum(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(twoSumL([2,7,11,15], 9), [0,1])
        self.assertEqual(twoSumD([2,7,11,15], 9), [0,1])

    def test_case_2(self):
        self.assertEqual(twoSumL([3,2,4,7,9], 6), [1,2])
        self.assertEqual(twoSumD([3,2,4,7,9], 6), [1,2])

    def test_case_3(self):
        self.assertEqual(twoSumL([1, 3, 5, 7, 9], 16), [3, 4])
        self.assertEqual(twoSumD([1, 3, 5, 7, 9], 16), [3, 4])
    
    def test_case_4(self):
        self.assertEqual(twoSumL([1, 1, 2, 3], 2), [0, 1])
        self.assertEqual(twoSumD([1, 1, 2, 3], 2), [0, 1])
    
    def test_case_5(self):
        self.assertEqual(twoSumL([-1, -2, -3, -4, -5], -8), [2, 4])
        self.assertEqual(twoSumD([-1, -2, -3, -4, -5], -8), [2, 4])

if __name__ == '__main__':
    unittest.main()