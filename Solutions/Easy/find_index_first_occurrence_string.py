# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)

# OR 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #if needle is an empty string, return 0
        if not needle:
            return 0
        # Getting the length of needle and haystack
        needle_len = len(needle)
        haystack_len = len(haystack)

        # Now we will itrate through haystack
        for i in range(haystack_len - needle_len + 1):
            # Checking if the substring of haystack starting at i matches needle
            if haystack[i:i + needle_len] == needle:
                return i # return the index of the first occurance
        
        # If needle is not found, retun -1
        return -1
    

# Example usage:
print(Solution().strStr("sadbutsad", "sad"))   # Output: 0
print(Solution().strStr("leetcode", "leeto"))  # Output: -1
print(Solution().strStr("hello", "ll"))        # Output: 2
print(Solution().strStr("aaaaa", "bba"))       # Output: -1
print(Solution().strStr("", ""))               # Output: 0
