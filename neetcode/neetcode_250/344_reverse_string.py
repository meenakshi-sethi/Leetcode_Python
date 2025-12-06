# LC 344 Reverse String
"""
LC Link: https://leetcode.com/problems/reverse-string/description/
NC Link: https://neetcode.io/solutions/reverse-string
"""

# Understanding the problem

"""
Given an array of characters s (in Python, this is a list of single-character strings).
We need to reverse the array in-place without allocating extra space for another array.

Key point for interview: The problem specifically requires O(1) extra space (excluding the input array).
This means we cannot create a new list - we must modify the existing one.
"""

# Approach 1: Using Python built-in function .reverse()
"""
Strategy: Use the list's built-in .reverse() method which modifies the list in-place.

Time Complexity: O(n) - reverses all n elements
Space Complexity: O(1) - no extra space used (modifies in-place)

Pros: Most concise and Pythonic, clearly shows intent
Cons: May not demonstrate algorithmic thinking in an interview setting
"""

def reverseString(s):
    s.reverse() # in-place modification and dont return


s = ["h","e","l","l","o"]
reverseString(s)
print(s)


# Approach 2: Brute force Approach - slicing - not optimal for this problem
"""
Strategy: Use slicing s[::-1] to create a reversed copy, then assign back using s[:].

Time Complexity: O(n) - creates reversed list + copies back
Space Complexity: O(n) - creates a temporary reversed list

Pros: Pythonic, short syntax
Cons: Violates the O(1) space requirement! Creates a new list internally.
"""

def reverseStringBF(s):
    reversed_s = s[::-1]        # creates a new reversed list
    for i in range(len(s)):
        s[i] = reversed_s[i]


# Approach 3: Two Pointer - optimal approach
"""
Strategy: Use two pointers - one at the start (left) and one at the end (right).
Swap elements at these positions and move pointers toward center until they meet.

Time Complexity: O(n) - we swap n/2 pairs of elements
Space Complexity: O(1) - only using two pointer variables

Pros: True O(1) space, demonstrates algorithmic thinking, great for interviews
Cons: Slightly more code than built-in methods

This is the solution that best demonstrates understanding of:
- Two pointer technique
- In-place array manipulation
- Space complexity optimization
"""

def reverseStringTP(s: List[str])-> None:
    left, right = 0, len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# Test cases
import unittest

class TestReverseString(unittest.TestCase):
    
    def test_case_1(self):
        # Example 1 from LC: odd length
        s1 = ["h", "e", "l", "l", "o"]
        s2 = ["h", "e", "l", "l", "o"]
        s3 = ["h", "e", "l", "l", "o"]
        
        reverseString(s1)
        reverseStringBF(s2)
        reverseStringTP(s3)
        
        self.assertEqual(s1, ["o", "l", "l", "e", "h"])
        self.assertEqual(s2, ["o", "l", "l", "e", "h"])
        self.assertEqual(s3, ["o", "l", "l", "e", "h"])
    
    def test_case_2(self):
        # Example 2 from LC: even length
        s1 = ["H", "a", "n", "n", "a", "h"]
        s2 = ["H", "a", "n", "n", "a", "h"]
        s3 = ["H", "a", "n", "n", "a", "h"]
        
        reverseString(s1)
        reverseStringBF(s2)
        reverseStringTP(s3)
        
        self.assertEqual(s1, ["h", "a", "n", "n", "a", "H"])
        self.assertEqual(s2, ["h", "a", "n", "n", "a", "H"])
        self.assertEqual(s3, ["h", "a", "n", "n", "a", "H"])
    
    def test_case_3(self):
        # Edge case: single character
        s1 = ["A"]
        s2 = ["A"]
        s3 = ["A"]
        
        reverseString(s1)
        reverseStringBF(s2)
        reverseStringTP(s3)
        
        self.assertEqual(s1, ["A"])
        self.assertEqual(s2, ["A"])
        self.assertEqual(s3, ["A"])
    
    def test_case_4(self):
        # Two characters
        s1 = ["a", "b"]
        s2 = ["a", "b"]
        s3 = ["a", "b"]
        
        reverseString(s1)
        reverseStringBF(s2)
        reverseStringTP(s3)
        
        self.assertEqual(s1, ["b", "a"])
        self.assertEqual(s2, ["b", "a"])
        self.assertEqual(s3, ["b", "a"])
    
    def test_case_5(self):
        # Palindrome - should remain same after reversal
        s1 = ["a", "b", "c", "b", "a"]
        s2 = ["a", "b", "c", "b", "a"]
        s3 = ["a", "b", "c", "b", "a"]
        
        reverseString(s1)
        reverseStringBF(s2)
        reverseStringTP(s3)
        
        self.assertEqual(s1, ["a", "b", "c", "b", "a"])
        self.assertEqual(s2, ["a", "b", "c", "b", "a"])
        self.assertEqual(s3, ["a", "b", "c", "b", "a"])

if __name__ == '__main__':
    unittest.main()