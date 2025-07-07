# https://leetcode.com/problems/majority-element/

# Approach 1: Frequency Count using Dictionary
"""
1. Initialize empty dictionary.
2. Iterate through the array (list)- for each element (key), increase its count (value) in the dictionary
3. After counting, find the key with the maximum frequency using get() method.
$. Return that key.

This works in O(n) time and O(n) space.
"""

def majorityElement(nums):
    count = {} # dictionary to store frequency

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    # Find the key with the maximum frequency
    majority = max(count,key = count.get)

    return majority

# Test cases
if __name__ == "__main__": # Run the code in this block only if this script is being run directly, not if it’s being imported.
    print(majorityElement([3,2,3])) # Output: 3
    print(majorityElement([2,2,1,1,1,2,2])) # Output: 2
    print(majorityElement([1])) # Output: 1
    print(majorityElement([1,2,3,4,5,5,5])) # Output: 5
    print(majorityElement([1,1,2,2,3,3,4,4,5])) # Output: 1 or 2 or 3 or 4 or 5 (any of the majority elements)      


# another pythonic way to do the same thing

def majorityElement1(nums):
    count = {} # dictionary to store frequency 

    for num in nums:
        count[num] = count.get(num,0) + 1 # Add 1 to the current count

    #find the key with maximum value
    return max(count, key = count.get)


# Test cases
print(majorityElement1([3,2,3])) # Output: 3
print(majorityElement1([2,2,1,1,1,2,2])) # Output: 2
print(majorityElement1([1])) # Output: 1
print(majorityElement1([1,2,3,4,5,5,5])) # Output: 5
print(majorityElement1([1,1,2,2,3,3,4,4,5])) # Output: 1 or 2 or 3 or 4 or 5 (any of the majority elements)