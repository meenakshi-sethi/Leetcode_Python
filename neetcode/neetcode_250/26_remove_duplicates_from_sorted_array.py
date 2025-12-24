# LC 26: Remove Duplicates from sorted array
"""
LC Link:https://leetcode.com/problems/remove-duplicates-from-sorted-array/
NC Link:https://neetcode.io/solutions/remove-duplicates-from-sorted-array
"""

# Understanding the problem
"""
Keep only one occurrence of each number, Maintain the original order, Since the array is sorted, all 
duplicates appear next to each other. return count of unique elements.

Why is sorting is important: Beacuse Duplicates are adjacent. Don't need hashing. Only compare current element
with previous one. So logic becomes: only keep an element if it is different from the last the last kept element

Step by step thinking
1. first element is always unique
2. start from second element
3. compare: current element ls[i] with last stored unique element
4. if different -> store it
5. if same -> skip it
"""

# Approach 1: Checking before appending by using in 
"""
Strategy: 
"""

def removeDup(ls):
    temp = []
    for i in range(0, len(ls)):
        if ls[i] not in temp:
                temp.append(ls[i])
    return temp, len(temp)


# Approach 2: Using 2 pointers
"""
Strategy: pointer j -> scanner: walks through the array and pointer i is writer -> marks position for the next unique element

j----nums[j]----nums[i-1]---------Action----------------nums-----------i---
1------20--------10-------------- different -> copy----[10, 20,..]------2---
2------20--------20-------------- same -> skip--------- unchanged ------2---
3------30--------20-------------- different -> copy----[10, 20, 30]-----3---
4------30--------30-------------- same -> skip -------- unchanged ------3---
5------40--------30-------------- different -> copy----[10,20,30,40,]---4---

Since the array is sorted, duplicates are adjacent.
I use two pointers: one to scan the array and another to track where the next unique element should be placed.
Whenever I find a new value, I overwrite the next position and increment the pointer.
Finally, the pointer gives me the count of unique elements.

Time complexity: O(n)
Space Complexity: O(1) (in place)
"""

def removeDuplicate(nums):
     if not nums:
          return 0
     
     i = 1
     for j in range(1, len(nums)):
          if nums[i-1] != nums[j]:
               nums[i] = nums[j]
               i += 1
     return i



import unittest

class TestRemoveDuplicates(unittest.TestCase):
     
     def assertRemoveDup(self, nums, expected_unique):
          """
          Helper:
          - run function
          - checks returned k
          - checks nums[:k] matches expected unique values
          """
          k = removeDuplicate(nums)
          self.assertEqual(k, len(expected_unique))
          self.assertEqual(nums[:k], expected_unique)
     
     def test_given_example(self):
          nums = [10, 20, 20, 30, 30, 30, 30, 40, 40, 50, 60]
          expected = [10, 20, 30, 40, 50, 60]
          self.assertRemoveDup(nums, expected)

     def test_no_duplicates(self):
          nums = [1,2,3,4]
          expected = [1,2,3,4]
          self.assertRemoveDup(nums, expected)
     
     def test_all_duplicates(self):
          nums = [7, 7, 7, 7]
          expected = [7]
          self.assertRemoveDup(nums, expected)

     def test_single_element(self):
          nums = [42]
          expected = [42]
          self.assertRemoveDup(nums, expected)

     def test_empty(self):
          nums = []
          expected = []
          self.assertRemoveDup(nums, expected)

     def test_negative_numbers(self):
          nums = [-3, -3, -2, -2, -2, 0 , 0, 5]
          expected = [-3, -2, 0, 5]
          self.assertRemoveDup(nums, expected)


if __name__ == "__main__":
     unittest.main()

