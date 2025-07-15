# https://leetcode.com/problems/valid-anagram/description/

'''
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the 
original letters exactly once.
eg Listen and Silent

'''

# Brute force approach - Using 2 dictionaries
'''
How to approach the problem
1. I will check if length of strings are equal if not we can return false. 
2. If length is same then I will initailise 2 empty dictionary
3. Will count the frequency of characters in both the string using for loop and .get() set the default value to zero and then increment 
4. Since python allows dictionary comparision I will compare the 2 dic usig ==
'''
import unittest

def validanagram(s: str, t:str):
    if len(s) != len(t): # to check if lengths are equal
        return False
    
    # creating 2 empty dictionary
    dict_s = {}
    dict_t = {}

    # for loop to count frequency
    for char in s:
        dict_s[char] = dict_s.get(char, 0) + 1
    
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    
    # compare dictionaries
    return dict_s == dict_t

class test_valid_anagram(unittest.TestCase):
    def testvalidanagrams(self):
        self.assertTrue(validanagram("anagram", "nagaram"))
        self.assertTrue(validanagram("listen", "silent"))
        self.assertTrue(validanagram("acca", "ccaa"))
        self.assertTrue(validanagram("", ""))  #edge case - empty string

    def testinvalidanagrams(self):
        self.assertFalse(validanagram("rat", "cat"))
        self.assertFalse(validanagram("hello", "bello"))  
        self.assertFalse(validanagram("a", "aa"))
        self.assertFalse(validanagram("acca", "cacc"))


if __name__ == '__main__':
    unittest.main()