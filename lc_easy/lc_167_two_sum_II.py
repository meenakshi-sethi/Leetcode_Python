# 167 two sum ii

"Approach: two pointers approach"


def twoSum(numbers, target):
    left, right = 0, len(numbers)-1 # zero based pointer

    while left < right:
        total = numbers[left] + numbers[right]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            return [left + 1 , right + 1] # convert to 1 based indexing
    return []


# time complexity = O(n) 
"""
We start with left at the start and right at the end of the array
In each iteration of the while loop: either left moves one step forward or right moves one step backward
this means each pointer moves at most n steps in total
hence total operation are proportional to n -> O(n). linear time
"""


