# https://leetcode.com/problems/fizz-buzz/description/

# Approach 1: Brute force using conditional statements

"""
Problem understanding:
Given an interger n and need to return a list of strings from 1 to n with the following rules:
    - If a number is divisible by 3 replace with "Fizz"
    - If divisible by 5 replace with "Buzz"
    - If divisible by both 3 & 5 replace with "FizzBuzz" 
    - Else keep the number as a string 

________________________________________________________________________________________________________________
How to approach the problem
I will use for loop with conditional statements
    1. Initialize an empty list called result to store the final FizzBuzz sequence.
    2. Loop through all numbers from 1 to n:
        - If a number is divisible by 3 replace with "Fizz"
        - If divisible by 5 replace with "Buzz"
        - If divisible by both 3 & 5 replace with "Fizzbuzz" 
        - Else keep the number as a string
    3. Return the result list

________________________________________________________________________________________________________________
Burte forece is also an optimal approach because the problem requires checking each number from 1 to n, hence must
visit all n elements.
Time Complexity: O(n)
Space Complexity: O(n)

"""
import unittest

def FizzBuzz(n):
    result = [] # empty list to store the sequence

    for i in range(1, n+1): # loop from 1 to n(inclusive)
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
        
    return result

# Test cases:
if __name__ == "__main__":
    print(FizzBuzz(5)) # Output: ['1', '2', 'Fizz', '4', 'Buzz']
    print(FizzBuzz(1))   # Output: ['1']
    print(FizzBuzz(0))   # Output: [] (edge case)

# Uint Test class

class TestFizzBuzz(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(FizzBuzz(5), ['1','2', 'Fizz', '4', 'Buzz'])

    def test_case_2(self):
        self.assertEqual(FizzBuzz(1), ['1'])

    def test_case_3(self):
        self.assertEqual(FizzBuzz(0), []) # edge case - 0 should return in empty list

    def test_case_4(self):
        expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        self.assertEqual(FizzBuzz(15), expected)


# Run the unit test
if __name__ == "__main__":
    unittest.main()

"""
What is a Unit Test?
A unit test is a small test written to check if a specific function or block of code works correctly.

- It tests one "unit" (e.g., a function) in isolation.
- If the function breaks or returns wrong results, the test will fail and report it.
- Unit tests help detect bugs early and ensure consistent behavior as code evolves.

Python has a built-in module called `unittest`

"""