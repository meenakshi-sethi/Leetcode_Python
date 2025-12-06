# LC_27_remove_elements
"""
LC Link:https://leetcode.com/problems/remove-element/description/
NC Link:https://neetcode.io/solutions/remove-element
"""

# Understanding problem
"""
Given a list nums and a number val, remove all val from the list in-place and return the new length.

"""
# Approach 1: Brute force - not in place modification
"""
Strategy: brute force approach solves the problem by creating a new list (tmp) that only includes the elements 
we want to keep (those not equal to val). Then, it copies the kept elements back into the beginning of the original array (nums).

Steps: 
1. Create an empty list, tmp.
2. Iterate through the original list (nums). If an element is not equal to the target value (val), append it to the tmp list.
3. Iterate through the tmp list and copy each element back to the beginning of the original nums list, starting at index 0.
4. Return the length of the tmp list, which represents the number of elements not equal to val.
"""

def removeElementsBF(nums: list, val:int)-> int:
    tmp = [] # temporary empty list

    for num in nums:# filter elements into new tmp list
        if num != val:
            tmp.append(num)

    for i in range(len(tmp)): # overwrite original list
        nums[i] = tmp[i]
    
    return len(tmp) # return new length


# Approach 2: Two Pointer 
"""
Strategy: use two pointers to modify the array in a single pass without allocating extra space. It treats the beginning of the list as the "write" area for the elements that do not equal the target value (val).
 - Read Pointer (i): Iterates through the entire array, checking every element.
 - Write Pointer (k): Tracks the position where the next non-val element should be placed (the new logical length of the array)

Steps: 
1. Start the write pointer, k, at index $0$. This pointer marks the location for the next valid element.
2. Use the read pointer, i, to loop from the beginning to the end of the array.
3. Conditional Overwrite: 
  - if the element at nums[i] is not equal to the target value (val), it means we want to keep it.
  - We then overwrite the element at nums[k] with nums[i].
  - Increment the write pointer k to prepare for the next element to keep.
4. The loop finishes, and the first k elements of nums now contain all the elements not equal to val. The value of k is the final count/length
"""

def removeElementsT(nums:list, val: int):
    k = 0 # write pointer which will overwrite non val element

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# Test cases
import unittest

class TestRemoveElement(unittest.TestCase):

    def test_case_1(self):
        nums1 = [3, 2, 2, 3]
        nums2 = [3, 2, 2, 3]

        self.assertEqual(removeElementsBF(nums1, 3), 2)
        self.assertEqual(nums1[:2], [2, 2])

        self.assertEqual(removeElementsT(nums2, 3), 2)
        self.assertEqual(nums2[:2], [2, 2])

    def test_case_2(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [1, 2, 3, 4]

        self.assertEqual(removeElementsBF(nums1, 5), 4)
        self.assertEqual(nums1[:4], [1, 2, 3, 4])

        self.assertEqual(removeElementsT(nums2, 5), 4)
        self.assertEqual(nums2[:4], [1, 2, 3, 4])

    def test_case_3(self):
        nums1 = [7, 7, 7]
        nums2 = [7, 7, 7]

        self.assertEqual(removeElementsBF(nums1, 7), 0)
        self.assertEqual(nums1[:0], [])

        self.assertEqual(removeElementsT(nums2, 7), 0)
        self.assertEqual(nums2[:0], [])

    def test_case_4(self):
        nums1 = [0,1,2,2,3,0,4,2]
        nums2 = [0,1,2,2,3,0,4,2]

        self.assertEqual(removeElementsBF(nums1, 2), 5)
        self.assertEqual(nums1[:5], [0,1,3,0,4])

        self.assertEqual(removeElementsT(nums2, 2), 5)
        self.assertEqual(nums2[:5], [0,1,3,0,4])

    def test_case_5(self):
        nums1 = [1, 1, 1, 2, 3]
        nums2 = [1, 1, 1, 2, 3]

        self.assertEqual(removeElementsBF(nums1, 1), 2)
        self.assertEqual(nums1[:2], [2, 3])

        self.assertEqual(removeElementsT(nums2, 1), 2)
        self.assertEqual(nums2[:2], [2, 3])


if __name__ == '__main__':
    unittest.main()