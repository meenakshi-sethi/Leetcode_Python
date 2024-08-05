# 9. Palindrome

class Solution:
    def isPalindrome(self, x: int) -> bool:
            if x < 0: # Negative numbers are not palindromes
                 return False
            front_num = x
            back_num = 0

            while x > 0:
                digit = x % 10
                back_num = back_num * 10 + digit
                x //= 10
            return front_num == back_num

# Creating an instance of the Solution class
sol = Solution()

# Test the isPalindrome method
print(sol.isPalindrome(121))  # Expected output: True
print(sol.isPalindrome(-121)) # Expected output: False
print(sol.isPalindrome(10))   # Expected output: False