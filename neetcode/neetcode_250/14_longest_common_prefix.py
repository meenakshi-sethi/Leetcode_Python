# LC 14 Longest Common Prefix

# Understanding the problem
"""
Given a list of words (strings), find the longest prefix that all of them share
Key points: prefix is beginning part of a word, it must be common to ALL words in the list, if no common prefix return empty string
if list is empty or has one word handle those edge cases
"""



# Approach 1: Horizonatal Scanning (Compare one by one using .find()) - worst time complexity O(S)
"""
Strategy: start by assuming the first word is you common prefix. Then compare it with the second word and trim it down until it matches.
then compare with the third word and trim again. Keep going until you have checked all words

Worst time complexity due to .find()
"""

def longestCommonPrefix_horizontal(strs):
    # Edge case: if list is empty, no common prefix exists
    if not strs:
        return ""
    
    # Step 1: Assume the first string is our prefix to start
    prefix = strs[0]
    print(f"Starting prefix: '{prefix}'")
    
    # Step 2: Compare this prefix with each remaining string
    for i in range(1, len(strs)):
        current_word = strs[i]
        print(f"\n--- Comparing with word {i}: '{current_word}' ---")
        
        # Keep shortening the prefix until it matches the start of current_word
        # The find() method returns the position where prefix is found
        # If prefix is at position 0, it means current_word starts with prefix
        while current_word.find(prefix) != 0:
            # Remove the last character from prefix
            prefix = prefix[:-1]
            print(f"  Trimming prefix to: '{prefix}'")
            
            # If prefix becomes empty, there's no common prefix
            if not prefix:
                print("  No common prefix found!")
                return ""
    
    print(f"\nFinal common prefix: '{prefix}'")
    return prefix

lists = ["Meenakshi", "Neha", "Medha", "Mukul", "Maan"]
longestCommonPrefix_horizontal(lists)

# Approach 2: Horizontal Scanning - compares character by character
"""
Strategy: Insted of repeatedly trimming the prefix until it matches (like with .find()), in this approach
- Start with the first string as the prefix.
- For each subsequent string, compares it character by character with the current prefix
- Finds where they differ and cuts the prefix at that point
- Continues with the shortened prefix for the next string

"""

def longestCommonPrefixH(strs: List[str])-> str:
    # step 1: start with the first string as our best guess for prefix
    prefix = strs[0] # prefix flower

    # step 2: check each remaining word
    for i in range(1, len(strs)):
        # i = 1 means we are looking at strs[1] which is "flow"
        # i = 2 means we are looking at strs[2] which is "flight"
        
        # step 3: start comparing from the beginning (position 0)
        j = 0

        # step 4: keep compating while we haven't reached the end
        while j <min(len(prefix), len(strs[i])):
            # this means while j is lessthan the length of the shorter word ***

            # step 5: compare characters at position j
            if prefix[j] != strs[i][j]:
                # if they don't match, STOP comparing
                break
            
            # step 6: they matched! move to next position
            j += 1 # this line is skipped if we broke above
        
        # step 7: cut prefix to only the part that matched
        prefix = prefix[:j]
        # its like saying keep only first j characters

    # step 8: return our final answer
    return prefix

"""
*** min(len(prefix), len(str[i])) -> We need to avoid comparing characters that don't exist. if we only checked one length we could try to access a character at a position that doesn't exist
-> Index out of range Error
"""

# Approach: 3 Vertical Scanning - comparing column by column
"""
Strategy: for each position i in first string, check if all strings have the same character at position i
- stop when a string is too short (i == len(s)) or characters dont match s[i] != strs[0][i]
Return the common part first i characters
"""

def longestCommonPrefixV(self, strs):
    # STEP 1: Loop through each position (column) in the FIRST string
    for i in range(len(strs[0])):
        # i = 0, 1, 2, 3, ... (checking each column)
        
        # STEP 2: Check this position in ALL strings
        for s in strs:
            # s = first string, second string, third string, etc.
            
            # STEP 3: Two conditions to stop:
            if i == len(s) or s[i] != strs[0][i]:
                # Condition 1: i == len(s) → We've reached the end of string s
                # Condition 2: s[i] != strs[0][i] → Characters don't match
                
                return s[:i]  # Return the common part (first i characters)
        
    # STEP 4: If we made it through all positions, the entire first string is the prefix
    return strs[0]
