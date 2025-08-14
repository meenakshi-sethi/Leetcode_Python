# lc 977 square of a sorted array

"""
Understanding the problem
Given a sorted array of integers nums (asc order). Some numbers can be negative. 
Square each number. When we square each number negative number becomes positive and as a result array which is not sorted
Need to return a sorted array of squares
"""

"""
Approach: Brute Force
- Square every element and sort the resulting list using sorted()
Time Complexity: O(n log n) (due to sorting)
Space Complexity: O(n) (new list for result)
Works fine but not optimal 
"""

def sortedSquaresBF(nums):
    return sorted(x*x for x in nums)

"""
Approach: Two pointer approach
The largest square will come from either the most negative number (big absolute value) or the largest positive number.
Since the array is sorted the largest absolute values will be at the ends.
Use two pointers (left at start, right at end) and fill the result array from the back.
"""
def sortedSquaresTP(nums):
    res = [] # empty array

    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            res.append(nums[left] * nums[left])
            left += 1
        else:
            res.append(nums[right] * nums[right])
            right -=1

    return res[::-1] # reversing the array


import unittest

class TestSortedSquares(unittest.TestCase):
    def testCases(self):
        self.assertEqual(sortedSquaresBF([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(sortedSquaresBF([-7,-3,-1]), [1,9,49])
        self.assertEqual(sortedSquaresBF([2,3,5]), [4,9,25])
        self.assertEqual(sortedSquaresBF([0]), [0])
        self.assertEqual(sortedSquaresBF([-1]), [1])
        self.assertEqual(sortedSquaresBF([-2, -1, -1, 0, 1, 1, 2]), [0, 1, 1, 1, 1, 4, 4])
        self.assertEqual(sortedSquaresBF([-3, -2, 0, 0, 1, 4]), [0, 0, 1, 4, 9, 16])
        self.assertEqual(sortedSquaresBF([-10000, 0, 10000]), [0, 100000000, 100000000])
        
        self.assertEqual(sortedSquaresTP([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(sortedSquaresTP([-7,-3,-1]), [1,9,49])
        self.assertEqual(sortedSquaresTP([2,3,5]), [4,9,25])
        self.assertEqual(sortedSquaresTP([0]), [0])
        self.assertEqual(sortedSquaresTP([-1]), [1])
        self.assertEqual(sortedSquaresTP([-2, -1, -1, 0, 1, 1, 2]), [0, 1, 1, 1, 1, 4, 4])
        self.assertEqual(sortedSquaresTP([-3, -2, 0, 0, 1, 4]), [0, 0, 1, 4, 9, 16])
        self.assertEqual(sortedSquaresTP([-10000, 0, 10000]), [0, 100000000, 100000000])

if __name__ == "__main__":
    unittest.main()
        
