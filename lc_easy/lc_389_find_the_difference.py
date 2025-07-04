#https://leetcode.com/problems/find-the-difference/description/

# Method 1: Using Sum of ASCII values
'''
We add up all ASCII codes in `t`, subtract the sum for `s`, and convert back with chr().
This works because `t` has one extra character.
Time Complexity: O(n), where n is the length of `t`.
Space Complexity: O(1), no extra space used.
'''
def findtheDifference(s:str, t:str):
    return chr(sum(map(ord, t))-sum(map(ord,s)))

# Test cases
print(findtheDifference("abcd", "abcde"))  # Output: 'e'
print(findtheDifference("", "y"))           # Output: 'y'
print(findtheDifference("a", "aa"))         # Output: 'a'
print(findtheDifference("ae", "aea"))       # Output: 'a'

