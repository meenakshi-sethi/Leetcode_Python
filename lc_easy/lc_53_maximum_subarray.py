# lc_53_maximum_subarray

def max_subarray(nums):
    max_sum = nums[0]
    curr_sum = 0

    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum

import unittest

class test_max_subarray(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(max_subarray([1]), 1)
        self.assertEqual(max_subarray([5,4,-1,7,8]), 23)
        self.assertEqual(max_subarray([-1,-2,-3,-4]), -1)
        self.assertEqual(max_subarray([0,0,0]), 0)
        self.assertEqual(max_subarray([8,-19,5,-4,20]), 21)



if __name__ == "__main__":
    unittest.main()