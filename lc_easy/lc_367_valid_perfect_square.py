# LC 367 Valid Perfect Square

# Brute Force approach
"""
start from i = 1 and check i * i == num return True
stop when i * i > num return False

Time complexity = O(sqrt n)
Space complexity = O(1)
"""

def isPerfectSquareBF(num):
    i = 1
    while i * i <= num: # keep squaring until we pass num
        if i * i == num:
            return True
        i += 1
    return False

"""
Dry run

num = 16
i=1 --> 1*1 = 1 != 16 (i*i <= nums, i+= 1 )
i=2 --> 2*2 = 4 != 16
i=3 --> 3*3 = 9 != 16
i=4 --> 4*4 = 16 = 16 Output True

num = 15
i=1 --> 1*1 = 1 != 15 (i*i <= nums, i+= 1 )
i=2 --> 2*2 = 4 != 15
i=3 --> 3*3 = 9 != 15
i=4 --> 4*4 = 16 > 15 Output False

"""
# Optimal Approach- Binary Search
"""
- Search for mid between 1 and num
- compare sq of mid (mid*mid) with num 
    - if equal return True
    - if smaller -> move left pointer towards right (left = mid + 1)
    - if greater -> move right pointer towards left (right = mid - 1)
- if not found -> return False

Time Complexity = O(log n)
Space Complexity = O(1)

=============================================================================================
What is binary search: 
Its a searching algorithm used to find an element in a sorted array/list by repeatedly dividing the seach range in half.
Instead of checking each element one by one (like linear search), BS eliminates half of the possibilites at every step.

How does it work?
1. Start with two pointer 
    - left = 0 (start of array)
    - right = n-1 (end of array)
2. Find the middle value --> middle = (left + right)//2 (#floor division)
3. Compare the middle element with target:
    - if arr[mid] == target --> found, return index
    - if arr[mid] > target --> search left half (right = mid - 1)
    - if arr[mid] < target --> search right half (left = mid + 1)
4. Repeat until left > right
    - if not found --> target doesn't exist in array

"""

def isPerfectSquareOP(num):
    if num == 1:
        return True         # special case as 1 is always 1 and we can save on iterations

    left, right = 1, num    # we will search between 1 and num

    # standard binary search loop
    while left <= right:
        mid = (left + right) // 2      # finding the middle value
        sq = mid * mid                 #square of middle value

        if sq == num:               # if mid*mid equals num then num is a perfect square
            return True
        elif sq < num:              # if mid*mid is smaller than num, we need a bigger number. Move search to the right side (left = mid + 1).
            left = mid + 1
        else:                       # if mid*mid is greater than num, we need a smaller number. Move search to the left side (right = mid - 1).
            right = mid - 1 
    return False                    # # If we finish the loop retrun False, it means no integer square matched num

"""
Dry Run
num = 16
left = 1, right  = 16
mid = (1+16)//2 = 8 --> 8^2 = 64 > 16 --> move left --> right = 7
mid = (1+7)//2 = 4 --> 4^2 = 16 == 16 --> Output True

"""

# Test cases

import unittest

class TestPerfectSquare(unittest.TestCase):
    def testCases(self):
        self.assertEqual(isPerfectSquareBF(25), True)
        self.assertEqual(isPerfectSquareBF(20), False)
        self.assertEqual(isPerfectSquareBF(1), True)
        self.assertEqual(isPerfectSquareBF(16), True)
        self.assertEqual(isPerfectSquareBF(14), False)
        self.assertEqual(isPerfectSquareBF(100), True)
        self.assertEqual(isPerfectSquareBF(99), False)

        self.assertEqual(isPerfectSquareOP(25), True)
        self.assertEqual(isPerfectSquareOP(20), False)
        self.assertEqual(isPerfectSquareOP(1), True)
        self.assertEqual(isPerfectSquareOP(16), True)
        self.assertEqual(isPerfectSquareOP(14), False)
        self.assertEqual(isPerfectSquareOP(100), True)
        self.assertEqual(isPerfectSquareOP(99), False)

        ## Both should give the same results

if __name__ == "__main__":
    unittest.main()