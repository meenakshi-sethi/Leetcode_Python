# LC 125 Valid Palindrome
"""
LC Link:https://leetcode.com/problems/valid-palindrome/description/
NC Link:https://neetcode.io/solutions/valid-palindrome
"""
# Understanding problem
"""
Palindrome = reads the same forward and backward (ignoring non-alphanumeric characters and case)
Given a string s, return true if it is a palindrome, otherwise return false

Tips: 
- Only consider alphanumeric characters (letters and numbers)
- Ignore case (treat 'A' and 'a' as the same)
- Ignore spaces, punctuation, and special characters

"""

# Approach 1: Preprocess + Reverse Compare - string concatenation
"""
Strategy: Clean the string by keeping only alphanumeric characters and converting to lowercase,
then compare the cleaned string with its reverse. The solution uses string concatenation which can be inefficient for large strings.

Time Complexity: O(n) where n is the length of the input string s
Space Complexity: O(n) for the cleaned string

"""

def isPalindrome(s):
    cleaned = "" 

    for char in s:
        if char.isalnum():
            cleaned += char.lower() 
    
    return cleaned == cleaned[::-1]

# Approach 2: List Comprehension + Join 
"""
Strategy: Use list comprehension to filter and convert characters,then join them into a string. Compare with its reverse.
More efficient than string concatenation as it avoids repeated string creation.

Time Complexity: O(n)
Space Complexity: O(n) for the cleaned string
"""
def isPalindromeComp(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

 
# Approach 3: Two Pointers with Custom Alphanumeric Check
"""
Strategy: Use two pointers starting from both ends. Skip non-alphanumeric characters using a custom helper function.
Compare valid characters while moving inward.

Time Complexity: O(n)
Space COmplexity: O(1)
"""
def isPalindromeCustom(s):
    def alphanum(char):
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )
    
    left, right = 0, len(s) -1

    while left < right:
        while left < right and not alphanum(s[left]):
            left += 1
        
        while left < right and not alphanum(s[right]):
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
    return True


# Approach 4: Two Pointers with Built-in isalnum()
"""
Strategy: Strategy: Same two-pointer approach but using Python's built-in isalnum() method.
More concise and Pythonic than the custom helper function.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def isPalindromeIs(s):
    left, right = 0, len(s) - 1 

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left > right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower(): 
            return False 
        
        left += 1
        right -= 1 
    
    return True 

# Approach 5: Two Pointers with Continue
"""
Strategy: Same two-pointer approach but uses if-continue pattern instead of nested while loops for skipping non-alphanumeric characters.
Some find this style more readable.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def isPalindromeOpt3(s):
    left, right = 0, len(s) -1 

    while left < right:
        if not s[left].isalnum(): 
            left += 1
            continue
        
        if not s[right].isalnum():
            right -= 1
            continue
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1 
        right -= 1
    
    return True


# Test cases

import unittest

class TestValidPalindrome_AllApproaches(unittest.TestCase):

    # Test cases for Approach 1: String Concatenation
    def test_valid_palindrome_concat(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(isPalindrome("racecar"))
        self.assertTrue(isPalindrome("Was it a car or a cat I saw?"))
        self.assertTrue(isPalindrome(" "))  # edge case: only spaces
        self.assertTrue(isPalindrome(""))   # edge case: empty string
        self.assertTrue(isPalindrome("a"))  # single character
        self.assertTrue(isPalindrome(".,"))  # only non-alphanumeric
        self.assertTrue(isPalindrome("A"))
        self.assertTrue(isPalindrome("Madam"))
        self.assertTrue(isPalindrome("nurses run"))

    def test_invalid_palindrome_concat(self):
        self.assertFalse(isPalindrome("race a car"))
        self.assertFalse(isPalindrome("hello"))
        self.assertFalse(isPalindrome("ab"))
        self.assertFalse(isPalindrome("0P"))
        self.assertFalse(isPalindrome("abc"))


    # Test cases for Approach 2: List Comprehension
    def test_valid_palindrome_comp(self):
        self.assertTrue(isPalindromeComp("A man, a plan, a canal: Panama"))
        self.assertTrue(isPalindromeComp("racecar"))
        self.assertTrue(isPalindromeComp("Was it a car or a cat I saw?"))
        self.assertTrue(isPalindromeComp(" "))
        self.assertTrue(isPalindromeComp(""))
        self.assertTrue(isPalindromeComp("a"))
        self.assertTrue(isPalindromeComp(".,"))
        self.assertTrue(isPalindromeComp("A"))
        self.assertTrue(isPalindromeComp("Madam"))
        self.assertTrue(isPalindromeComp("nurses run"))

    def test_invalid_palindrome_comp(self):
        self.assertFalse(isPalindromeComp("race a car"))
        self.assertFalse(isPalindromeComp("hello"))
        self.assertFalse(isPalindromeComp("ab"))
        self.assertFalse(isPalindromeComp("0P"))
        self.assertFalse(isPalindromeComp("abc"))


    # Test cases for Approach 3: Two Pointers with Custom Check
    def test_valid_palindrome_custom(self):
        self.assertTrue(isPalindromeCustom("A man, a plan, a canal: Panama"))
        self.assertTrue(isPalindromeCustom("racecar"))
        self.assertTrue(isPalindromeCustom("Was it a car or a cat I saw?"))
        self.assertTrue(isPalindromeCustom(" "))
        self.assertTrue(isPalindromeCustom(""))
        self.assertTrue(isPalindromeCustom("a"))
        self.assertTrue(isPalindromeCustom(".,"))
        self.assertTrue(isPalindromeCustom("A"))
        self.assertTrue(isPalindromeCustom("Madam"))
        self.assertTrue(isPalindromeCustom("nurses run"))

    def test_invalid_palindrome_custom(self):
        self.assertFalse(isPalindromeCustom("race a car"))
        self.assertFalse(isPalindromeCustom("hello"))
        self.assertFalse(isPalindromeCustom("ab"))
        self.assertFalse(isPalindromeCustom("0P"))
        self.assertFalse(isPalindromeCustom("abc"))


    # Test cases for Approach 4: Two Pointers with isalnum()
    def test_valid_palindrome_is(self):
        self.assertTrue(isPalindromeIs("A man, a plan, a canal: Panama"))
        self.assertTrue(isPalindromeIs("racecar"))
        self.assertTrue(isPalindromeIs("Was it a car or a cat I saw?"))
        self.assertTrue(isPalindromeIs(" "))
        self.assertTrue(isPalindromeIs(""))
        self.assertTrue(isPalindromeIs("a"))
        self.assertTrue(isPalindromeIs(".,"))
        self.assertTrue(isPalindromeIs("A"))
        self.assertTrue(isPalindromeIs("Madam"))
        self.assertTrue(isPalindromeIs("nurses run"))

    def test_invalid_palindrome_is(self):
        self.assertFalse(isPalindromeIs("race a car"))
        self.assertFalse(isPalindromeIs("hello"))
        self.assertFalse(isPalindromeIs("ab"))
        self.assertFalse(isPalindromeIs("0P"))
        self.assertFalse(isPalindromeIs("abc"))


    # Test cases for Approach 5: Two Pointers with Continue
    def test_valid_palindrome_opt3(self):
        self.assertTrue(isPalindromeOpt3("A man, a plan, a canal: Panama"))
        self.assertTrue(isPalindromeOpt3("racecar"))
        self.assertTrue(isPalindromeOpt3("Was it a car or a cat I saw?"))
        self.assertTrue(isPalindromeOpt3(" "))
        self.assertTrue(isPalindromeOpt3(""))
        self.assertTrue(isPalindromeOpt3("a"))
        self.assertTrue(isPalindromeOpt3(".,"))
        self.assertTrue(isPalindromeOpt3("A"))
        self.assertTrue(isPalindromeOpt3("Madam"))
        self.assertTrue(isPalindromeOpt3("nurses run"))

    def test_invalid_palindrome_opt3(self):
        self.assertFalse(isPalindromeOpt3("race a car"))
        self.assertFalse(isPalindromeOpt3("hello"))
        self.assertFalse(isPalindromeOpt3("ab"))
        self.assertFalse(isPalindromeOpt3("0P"))
        self.assertFalse(isPalindromeOpt3("abc"))


    # Additional edge case tests for all approaches
    def test_numbers_only_all_approaches(self):
        """Test with numeric palindromes"""
        self.assertTrue(isPalindrome("12321"))
        self.assertTrue(isPalindromeComp("12321"))
        self.assertTrue(isPalindromeCustom("12321"))
        self.assertTrue(isPalindromeIs("12321"))
        self.assertTrue(isPalindromeOpt3("12321"))

    def test_mixed_alphanumeric_all_approaches(self):
        """Test with mixed letters and numbers"""
        self.assertTrue(isPalindrome("A1b2B1a"))
        self.assertTrue(isPalindromeComp("A1b2B1a"))
        self.assertTrue(isPalindromeCustom("A1b2B1a"))
        self.assertTrue(isPalindromeIs("A1b2B1a"))
        self.assertTrue(isPalindromeOpt3("A1b2B1a"))

    def test_special_characters_all_approaches(self):
        """Test with lots of special characters"""
        self.assertTrue(isPalindrome("!@#$$#@!"))
        self.assertTrue(isPalindromeComp("!@#$$#@!"))
        self.assertTrue(isPalindromeCustom("!@#$$#@!"))
        self.assertTrue(isPalindromeIs("!@#$$#@!"))
        self.assertTrue(isPalindromeOpt3("!@#$$#@!"))


if __name__ == '__main__':
    unittest.main()