# LC 1299 Replace Elements with Greatest Element on Right Side

# My approach using max() brute force
"""
using for loop iterate through the array and every item i will compare with max element from remaining array we replace the vslue of i with max.  

for each index 'i' in `arr`:
 - take the slice arr[i+1:] (everything to the right)
 - find max using max(arr[i+1:])
 - replace `arr[i]` with that maximum
 - for last element just replace with -1
Time complexity = O(n^2) & Space Complexity = O(1) in place
"""

def replaceElementsBF(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i] = -1 # setting last element
        else:
            arr[i] = max(arr[i+1:]) # max of the remaining array
    return arr 

"""
Dry Run

For arr = [17,18,5,4,6,1]:

i=0 → arr[0] = max([18,5,4,6,1]) = 18

i=1 → arr[1] = max([5,4,6,1]) = 6

i=2 → arr[2] = max([4,6,1]) = 6

i=3 → arr[3] = max([6,1]) = 6

i=4 → arr[4] = max([1]) = 1

i=5 → arr[5] = -1

Output = [18,6,6,6,1,-1]
"""

import unittest

class TestReplaceElements(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(replaceElementsBF([17,18,5,4,6,1]), [18,6,6,6,1,-1])
        self.assertEqual(replaceElementsBF([400]), [-1])
        self.assertEqual(replaceElementsBF([1,2,3,4,5]), [5,5,5,5,-1])
        self.assertEqual(replaceElementsBF([5,4,3,2,1]), [4,3,2,1,-1])
        self.assertEqual(replaceElementsBF([7,7,7]), [7,7,-1])
        self.assertEqual(replaceElementsBF([9,1]), [1,-1])
        self.assertEqual(replaceElementsBF([100000, 99999]), [99999, -1])

if __name__ == "__main__":
    unittest.main()


# Optimal approach
"""
Right-to-Left Scan
Instead of recalculating max everytime track from right to left:
- Initialize maxRight = -1 (because last element must become -1)
- Traverse from rightmost element to leftmost:
   - Save the current element in a temp variable
   - replace current element with maxRight
   - Update maxRight = max(maxRight, temp)

Time complexity = O(n) and Space complexity = O(1)
"""

def replaceElementsOP(arr):
    maxRight = -1 # last element should always be -1

    for i in range(len(arr)-1, -1, -1): # iterate from right to left
        newMax = max(maxRight, arr[i]) # precompute the new max
        arr[i] = maxRight # replace with old rightMax
        maxRight = newMax # update rightMax
    return arr

class TestReplaceElements(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(replaceElementsOP([17,18,5,4,6,1]), [18,6,6,6,1,-1])
        self.assertEqual(replaceElementsOP([400]), [-1])
        self.assertEqual(replaceElementsOP([1,2,3,4,5]), [5,5,5,5,-1])
        self.assertEqual(replaceElementsOP([5,4,3,2,1]), [4,3,2,1,-1])
        self.assertEqual(replaceElementsOP([7,7,7]), [7,7,-1])
        self.assertEqual(replaceElementsOP([9,1]), [1,-1])
        self.assertEqual(replaceElementsOP([100000, 99999]), [99999, -1])

if __name__ == "__main__":
    unittest.main()



