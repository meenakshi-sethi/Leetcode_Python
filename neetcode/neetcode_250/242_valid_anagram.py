# LC_242 Valid Anagram
"""
LC link: https://leetcode.com/problems/valid-anagram/description/
NC link: https://neetcode.io/solutions/valid-anagram
"""


# Understanding problem
"""
Anagram = same characters, same frequency, different order
given 2 strings s and t, return true if t is an anagram of s otherwise return false

tip: if lengths differ immediately return false


"""

# Approach 1: Using sorting approach
"""
strategy: sort both strings and compare will automatically give True or False

"""

def isAnagramS(s:str, t:str):
    return sorted(s)== sorted(t)


# Approach 2: Using Counter `collections.Counter`
from collections import Counter

def isAnagramC(s:str, t:str):
    return Counter(s) == Counter(t)


# Approach 3: Counting Characters (dictionary i.e hashmap) - manual counting
"""
Strategy: Count the frequency of each character in s and t and then compare the 2 dictionary.

"""

def isAnagramH(s:str, t:str):
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for char in s:
        crr_countS = countS.get(char, 0)
        countS[char] = crr_countS + 1
    
    for char in t:
        crr_countT = countT.get(char, 0)
        countT[char] = crr_countT + 1
    
    return countS == countT


# Test cases

import unittest

class TestValidAnagram_AllApproaches(unittest.TestCase):

    # for Approach 1: Sorting
    def test_valid_anagram_sorting(self):
        self.assertTrue(isAnagramS("anagram", "nagaram"))
        self.assertTrue(isAnagramS("listen", "silent"))
        self.assertTrue(isAnagramS("acca", "ccaa"))
        self.assertTrue(isAnagramS("", ""))  # edge case

    def test_invalid_anagram_sorting(self):
        self.assertFalse(isAnagramS("rat", "cat"))
        self.assertFalse(isAnagramS("hello", "bello"))
        self.assertFalse(isAnagramS("a", "aa"))
        self.assertFalse(isAnagramS("acca", "cacc"))
        self.assertFalse(isAnagramS("Abc", "abc"))  # case sensitivity


    # for Approach 2: Counter
    def test_valid_anagram_counter(self):
        self.assertTrue(isAnagramC("anagram", "nagaram"))
        self.assertTrue(isAnagramC("listen", "silent"))
        self.assertTrue(isAnagramC("acca", "ccaa"))
        self.assertTrue(isAnagramC("", ""))

    def test_invalid_anagram_counter(self):
        self.assertFalse(isAnagramC("rat", "cat"))
        self.assertFalse(isAnagramC("hello", "bello"))
        self.assertFalse(isAnagramC("a", "aa"))
        self.assertFalse(isAnagramC("acca", "cacc"))
        self.assertFalse(isAnagramC("Abc", "abc"))


    # for Approach 3: Hashmap / Manual Counting
    def test_valid_anagram_hashmap(self):
        self.assertTrue(isAnagramH("anagram", "nagaram"))
        self.assertTrue(isAnagramH("listen", "silent"))
        self.assertTrue(isAnagramH("acca", "ccaa"))
        self.assertTrue(isAnagramH("", ""))

    def test_invalid_anagram_hashmap(self):
        self.assertFalse(isAnagramH("rat", "cat"))
        self.assertFalse(isAnagramH("hello", "bello"))
        self.assertFalse(isAnagramH("a", "aa"))
        self.assertFalse(isAnagramH("acca", "cacc"))
        self.assertFalse(isAnagramH("Abc", "abc"))


if __name__ == '__main__':
    unittest.main()
