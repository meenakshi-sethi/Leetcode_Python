# lc 290 Word Pattern

def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False
    
    # creating 2 dictionaries
    charToWord = {} # empty dict to map char to word
    wordToChar = {} # empty dict to map word to char

    for c, w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w:
            return False
        if w in wordToChar and wordToChar[w] != c:
            return False
        charToWord[c] = w
        wordToChar[w] = c
    return True


import unittest

class TestWordPattern(unittest.TestCase):
    def test_case(self):
        self.assertEqual(wordPattern("abba", "dog cat cat dog"), True)
        self.assertEqual(wordPattern("abba", "dog cat cat fish"), False)
        self.assertEqual(wordPattern("aaaa", "dog cat cat dog"), False)
        self.assertEqual(wordPattern("abba", "dog dog dog dog"), False)
        self.assertEqual(wordPattern("abba", "dog cat cat"), False)
        self.assertEqual(wordPattern("a", "dog"), True)
        self.assertEqual(wordPattern("abcabc", "red blue green red blue green"), True)
        self.assertEqual(wordPattern("abba", "dog   cat   cat   dog"), True)  # handles multiple spaces
        self.assertEqual(wordPattern("abc", "x\ty\nz"), True)  # handles tabs & newlines
        self.assertEqual(wordPattern("abca", "dog cat cat dog"), False)  # non-bijective mapping

if __name__ == "__main__":
    unittest.main()