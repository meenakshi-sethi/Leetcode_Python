# 14 Longest common prefix

class Solution:
    def longestCommonPrefix(self, strs: List(str)) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]

        for s in strs[1:]:
            while s[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# Test Cases
solution = Solution()

# Example 1
strs = ["flower", "flow", "flight"]
print(f"Input: {strs}, Output: {solution.longestCommonPrefix(strs)}")  # Output: "fl"

# Example 2
strs = ["dog", "racecar", "car"]
print(f"Input: {strs}, Output: {solution.longestCommonPrefix(strs)}")  # Output: ""



