# preprocess + reverse-compare solution

def isPalindrome(s):
    cleaned = "" # creating an empty string to store cleaned characters

    for char in s: # loop through each character in the input string
        if char.isalnum(): # checking if the character is alphanumeric
            cleaned += char.lower() # converting the character to lower case and adding it to cleaned
    
    return cleaned == cleaned[::-1] # reversing the cleaned string and return Ture if cleaned string equal its reverse

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama")) # Expected Output: True
print(isPalindrome("race a car")) # Expected Output: False
print(isPalindrome(" ")) # Expected Output: True
print(isPalindrome("0P")) # Expected Output: False 
print(isPalindrome("A")) # Expected Output: True
print(isPalindrome("abccba")) # Expected Output: True

# Time Complexity: O(n) where n is the length of the input string s
# Space Complexity: O(n) for the cleaned string
# Note: The solution uses string concatenation which can be inefficient for large strings.

# Alternative solution using list comprehension and join
def isPalindromeAlt(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Test cases for the alternative solution
print(isPalindromeAlt("A man, a plan, a canal: Panama")) # Expected Output: True
print(isPalindromeAlt("race a car")) # Expected Output: False
print(isPalindromeAlt(" ")) # Expected Output: True
print(isPalindromeAlt("0P")) # Expected Output: False 
print(isPalindromeAlt("A")) # Expected Output: True
print(isPalindromeAlt("abccba")) # Expected Output: True
# Time Complexity: O(n)
# Space Complexity: O(n) for the cleaned string 
## Note: This solution is more efficient in terms of string handling as it avoids repeated concatenation.


# Optimized solution using two pointers Option 1
def isPalindromeOpt1(s):
    l, r = 0, len(s) -1

    while l < r:
        while l< r and not alphanum(s[l]):
            l += 1
        
        while r > l and not alphanum(s[r]):
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
    return True

# helper function to check if a character is alphanumeric
def alphanum(char):
    return (
        ord('A') <= ord(char) <= ord('Z') or
        ord('a') <= ord(char) <= ord('z') or
        ord('0') <= ord(char) <= ord('9')
    )


# Test cases
print(isPalindromeOpt1("A man, a plan, a canal: Panama")) # Expected Output: True
print(isPalindromeOpt1("race a car")) # Expected Output: False
print(isPalindromeOpt1(" ")) # Expected Output: True
print(isPalindromeOpt1("0P")) # Expected Output: False 
print(isPalindromeOpt1("A")) # Expected Output: True
print(isPalindromeOpt1("abccba")) # Expected Output: True

# Time Complexity: O(n) where n is the length of the input string s
# Space Complexity: O(1) since we are using two pointers and not creating any additional data structures (string)
# Note: This solution is more efficient than the previous ones as it uses two pointers to traverse the string from both ends, reducing the need for additional space.


# Optimized solution using two pointers Option 2 (without helper function using inbuilt function)
def isPalindromeOpt2(s):
    left = 0 # Pointer starting from the beginning of the string
    right = len(s) - 1 # Pointer starting fron the end of the string

    # We move both pointers inward, skipping non -aplhanumeric characters and compare the valid characters
    while left < right:
        while left < right and not s[left].isalnum(): # Skip non alphanumeric characters from the left
            left += 1

        while left > right and not s[right].isalnum(): # skip non alphanumeric characters from the right
            right -= 1
        
        if s[left].lower() != s[right].lower(): # comapre lowercase version of the characters
            return False # if they are not equal return False, not a palindrome
        
        left += 1 # move the left pointer inward
        right -= 1 # move the right pointer inward
    
    return True # if we reach here, it means the string is a palindrome

print(isPalindromeOpt2("A man, a plan, a canal: Panama")) # Expected Output: True
print(isPalindromeOpt2("race a car")) # Expected Output: False
print(isPalindromeOpt2(" ")) # Expected Output: True
print(isPalindromeOpt2("0P")) # Expected Output: False 
print(isPalindromeOpt2("A")) # Expected Output: True
print(isPalindromeOpt2("abccba")) # Expected Output: True

# Time Complexity: O(n) where n is the length of the input string s
# Space Complexity: O(1) since we are using two pointers and not creating any additional data structures (string)
# Note: This solution is efficient and straightforward, leveraging Python's built-in string methods to handle character checks and comparisons.

# Optimized solution using two pointers Option 3 (without helper function using inbuilt function)
def isPalindromeOpt3(s):
    left = 0 # Pointer starting from the beginning of the string
    right = len(s) - 1 # Pointer starting from the end of the string

    while left < right:
        if not s[left].isalnum(): # Skip non-alphanumeric characters from the left
            left += 1
            continue
        
        if not s[right].isalnum(): # Skip non-alphanumeric characters from the right
            right -= 1
            continue
        
        if s[left].lower() != s[right].lower(): # Compare lowercase version of the characters
            return False # If they are not equal, return False, not a palindrome
        
        left += 1 # Move the left pointer inward
        right -= 1 # Move the right pointer inward
    
    return True # If we reach here, it means the string is a palindrome

# Time Complexity: O(n) where n is the length of the input string s
# Space Complexity: O(1) since we are using two pointers and not creating any additional data structures (string)
# Note: This solution is similar to Option 2 but uses `if` statements with `continue` to handle skipping non-alphanumeric characters, which can be more readable for some.

'''
Comparison of Option while & while vs while & if + contiunue

| Feature                  | Option 1: Inner `while`             | Option 2: `if` + `continue`         |
| ------------------------ | ----------------------------------- | ----------------------------------- |
| Clarity                  | Slightly more concise when skipping | More readable and beginner-friendly |
| Logic                    | Efficient: skips multiple in one go | Same logic, but uses `continue`     |
| Loop Efficiency          | Keeps skipping until valid char     | Handles one invalid char at a time  |
| Control Flow             | Cleaner linear flow                 | More jumpy with `continue`          |
| Best for Learning        | May look complex at first           | Easier to follow for beginners      |
| Performance              | Slightly faster if many invalids    | Very close; negligible difference   |

# Both options are efficient and have the same time complexity of O(n) and space complexity of O(1).   
'''