#LC 705_ Group Anagram
"""
LC link: https://leetcode.com/problems/group-anagrams/
NC Link: https://neetcode.io/solutions/group-anagrams

"""

# Understanding Problem
"""
We need to group words that are anagrams
"""

# Approach 1: Sorting
"""
Strategy

Time Complexity: O(nlogn * m)
Space Complexity: O(m+n)
"""

def groupAnagram(self, strs):
    result = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        result[sortedS].append(s)
    return list(res.values())

# Approach 2: Hash Table

