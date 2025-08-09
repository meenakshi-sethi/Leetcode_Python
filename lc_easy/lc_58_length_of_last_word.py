# lc 58 length of last word in a string

# Approach - start from the last and count characters and as soon as we find space we need to exit the loop and return the counter value.

def lengthOfLastWord(s):
    length = 0 # stores the length of last word
    i = len(s) - 1 #starting from last index

    # Skip trailing spaces
    while s[i] == " ":
        i -= 1 # to move towards left

    # counts the last word
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1 
    return length



import unittest

class TestLengthOfLastWord(unittest.TestCase):
    def test_case(self):
        self.assertEqual(lengthOfLastWord("Hello World"), 5)
        self.assertEqual(lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(lengthOfLastWord("luffy is still joyboy"), 6)
        self.assertEqual(lengthOfLastWord("a "), 1)
        self.assertEqual(lengthOfLastWord("Python"), 6)

if __name__ == "__main__":
    unittest.main() 
    
