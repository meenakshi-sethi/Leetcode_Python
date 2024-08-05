class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Stack to keep track of opening brackets
        mapping = {')': '(', '}': '{', ']': '['} # Mapping of closing to opening brackets

        # Iterate through each character in the string
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#' # Pop from stack if not empty, else use dummy value
                if mapping[char] != top_element: # Check if the popped element matches the mapping
                    return False
            else:
                stack.append(char) # Push opening brackets onto the stack
        
        return not stack # Return True if stack is empty (all brackets matched)

# Example usage:
sol = Solution()
print(sol.isValid("()"))  # Output: true
print(sol.isValid("()[]{}"))  # Output: true
print(sol.isValid("(]"))  # Output: false