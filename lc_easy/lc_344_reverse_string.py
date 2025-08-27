# LC 344 Reverse String

"""
Understanding the problem

Given a string which is an array of characters s. In python that means a list of single - character strings
We need to reverse the array in place (i.e modify the same array and not creating a new one)

"""

# Approach
"""
Input is an array of characters its not a string its a list. 
So i will be using `.reverse()` it works in place on list (which is exactly the problem is asking)
"""

def reverseString(s):
    "do no return anything, modify s in place instead"
    s.reverse()


s = ["h","e","l","l","o"]
reverseString(s)
print(s)


# Brute force Approach
"""
Using slicing: s[:] = s[::-1]
Pythonic but it internally creates a new reversed list before copying back. not optimal for interview setting (space isn't O(1))
"""

def reverseStringBF(s):
    reversed_s = s[::-1]        # creates a new reversed list
    for i in range(len(s)):
        s[i] = reversed_s[i]

s1 = ["h","e","l","l","o"]
reverseStringBF(s1)
print(s1)


# Optimal Approach: Two Pointer

