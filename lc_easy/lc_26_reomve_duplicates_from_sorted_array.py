# https://github.com/xizhang20181005/Leetcode_company_frequency

# Approach 1: Two Pointer Approach
"""
Right pointer sacns the array and left pointer keeps track of where the next unique element shoud go.
"""

def removeDuplicates(nums):
    if not nums:
        return 0 # if the array is empty, return 0
    
    left = 1 # strat from index 1 because nums[0] is always unique

    for right in range(1, len(nums)): # for every right from 1 to end of array
        if nums[right] != nums[right -1]: # check if nums[right] is not equal to the previous element (nums[right-1])
            nums[left] = nums[right] # if unique assign it to nums[left] and move left pointer forward to next slot. if duplicate skip it.
            left += 1
    
    return left # retund the number of unique elements, nums[0:left]

# Test cases
print(removeDuplicates([1, 1, 2]))  # Output: 2
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # Output: 5
print(removeDuplicates([1, 2, 3, 4, 5]))  # Output: 5
print(removeDuplicates([]))  # Output: 0
print(removeDuplicates([1, 1, 1, 1, 1]))  # Output: 1

'''
__main__ = "__main__"
if __name__ == "__main__":
    # Example usage
    nums = [1, 1, 2, 2, 3]
    length = removeDuplicates(nums)
    print(f"Length of array after removing duplicates: {length}")
    print(f"Array after removing duplicates: {nums[:length]}")
'''

# Time Complexity: O(n), where n is the length of the input array.
# Space Complexity: O(1), since we are modifying the input array in place.


