# LC 374 Guess Number Higher or Lower

"""
Understandign the problem:
We are playing a game: Guess the number. The system picks a number between 1 and n. I (as player) have to guess it.
Each time i guess there is a provided API guess(num) that returns: -1 if systems picked number is lower than my guess, 1 if systems picked number is higher than my guess 
and 0 if my guess is correct.
I need to return the picked number by system

point to note # The guess API is already defined for you.

to check my solution we need to run this in leetcode 

"""
# Binary search

class Solution:
    def guessNumber(self, n:int) -> int:
        l, r = 1, n

        while True: # taking true becasue problem gaurantees a solution in the given range.
            m = (l + r)// 2
            result = guess(m)
            if result > 0:
                l = m + 1
            elif result < 0:
                r = m - 1
            else:
                return m
