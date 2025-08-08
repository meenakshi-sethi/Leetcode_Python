#lc_20_valid_parantheses


def validparan(s):
    stack = [] # empty list (stack)
    pairs = {")":"(", "]": "[", "}":"{"} # dict of parantheses

    for char in s:
        if char in pairs:
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
        else: #for open parantheses
            stack.append(char)
    return True if not stack else False

import unittest

class test_validparan(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(validparan("()"), True)
        self.assertEqual(validparan("()"), True)         
        self.assertEqual(validparan("()[]{}"), True)     
        self.assertEqual(validparan("(]"), False)        
        self.assertEqual(validparan("([)]"), False)      
        self.assertEqual(validparan("{[]}"), True)       
        self.assertEqual(validparan("("), False) 


if __name__ == "__main__":
    unittest.main()
