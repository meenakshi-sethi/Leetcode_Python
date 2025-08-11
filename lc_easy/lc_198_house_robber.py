# LC 198. House Robber (Dynamic Programming)

"""
What the problem is saying in plain English
Imagine a row of houses, each with some amount of cash.
We want to rob houses to get the most money possible.
Rule: We cannot rob two houses in a row — if we do, an alarm goes off.


Summary of question: 
Given: An array nums where nums[i] is the amount of money in the i-th house.
Rule: We cannot rob two adjacent houses.
Goal: Return the maximum money you can rob without triggering the alarm.



My approach

Constraint: No two house can be robbed. this means if we rob house i, we must skip house i-1 and go for i-2.

Brute force: Try all combinations using recursion. Rob  current house --> skip next. Skip current house --> rob next. Time complexity O(2^n)
Dynamic Programing: max money upto house i depends only on: 
    i. Robbing i --> money from i + best we can do till i-2
    ii. Skipping i --> best we can do till i-1


"""

# Space Optimized O(1) space version 

def rob_opt(nums):
    # rob1-> best amount if you consider houses upto i-2, rob2 -> best amount if you consider houses up to i-1.
    rob1, rob2 = 0, 0 # Rob1= No houses two step back yet, Rob2= No houses considered yet     

    # (rob1, rob2, n, n+1, ....)
    for n in nums:
        temp = max(n+rob1, rob2) # n+rob1 -> Rob current house (skip previous house, so add value from i-2), rob2 -> skip current house, best so far without robbing this one
        rob1 = rob2 # Shift rob1 to the previous rob2
        rob2 = temp # rob2 becomes the best so far
    return rob2 # time and space complexity O(n) & O(1)

# Classic DP array version

def rob_dp_array(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i]+ dp[i-2])
    return dp[-1]



# Test cases
import unittest
import random

class testRob(unittest.TestCase):
    def testcases(self):
        tests = [
            ([], 0),                              # no houses
            ([5], 5),                             # single house
            ([2, 3], 3),                          # pick the larger of two
            ([1, 2, 3, 1], 4),                    # 1 + 3
            ([2, 7, 9, 3, 1], 12),                # 2 + 9 + 1
            ([2, 1, 1, 2], 4),                    # 2 + 2 (ends)
            ([10, 1, 1, 10], 20),                 # 10 + 10
            ([0, 0, 0], 0),                       # all zeros
            ([100, 1, 1, 100, 1], 200),           # big ends
            ([1, 3, 1, 3, 100], 103),             # 3 + 100
        ]
        for nums, expected in tests:
                self.assertEqual(rob_opt(nums), expected)
                self.assertEqual(rob_dp_array(nums), expected)

    def test_random(self):
        for _ in range(50):
            nums = [random.randint(0, 20) for _ in range(random.randint(0, 15))]
            self.assertEqual(rob_opt(nums), rob_dp_array(nums))

if __name__ == "__main__":
    unittest.main()


