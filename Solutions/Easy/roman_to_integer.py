#13 Romnan to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        for i in range(len(s)):
            if i < len(s) - 1 and romanToInt[s[i]] < romanToInt[s[i+1]]:
                total -= romanToInt[s[i]]
            else:
                total += romanToInt[s[i]]
        return total

# Test method
sol = Solution()
print(sol.romanToInt("III"))     # Expected output: 3
print(sol.romanToInt("LVIII"))   # Expected output: 58
print(sol.romanToInt("MCMXCIV")) # Expected output: 1994  
