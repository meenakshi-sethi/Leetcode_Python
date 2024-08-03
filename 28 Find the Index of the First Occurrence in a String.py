class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
# Example usage:
print(Solution().strStr("sadbutsad", "sad"))   # Output: 0
print(Solution().strStr("leetcode", "leeto"))  # Output: -1
print(Solution().strStr("hello", "ll"))        # Output: 2
print(Solution().strStr("aaaaa", "bba"))       # Output: -1
print(Solution().strStr("", ""))               # Output: 0