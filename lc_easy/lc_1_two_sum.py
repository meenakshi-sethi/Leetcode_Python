# https://leetcode.com/problems/two-sum/description/

# brute force approach
'''
To solve this problem I am using brute force method. I loop through each number in the list using index i. 
For each `i` I loop through all numbers that come after it using indes `j`. There will be 2 for loops one 
for outer loop and one for inner loop. Outer loop goes through each element one by one and inner loop checks
all the elements after the current element. if the sum of nums[i] + nums[j] equals the traget, I return the 
indices [i,j].
As question says  there is exactly one solution, I can return as soon as i find a match. 
'''
def two_sum(nums, target):
    for i in range(len(nums)): # loop that starts from 0th indes that is first element of list
        for j in range(i + 1, len(nums)): # loop that starts from i+1th index i.e 2nd element of the list
            if nums[i] + nums[j] == target: # condition to check if sum of 2 elements is equal to target
                return [i, j] # if match found then return indexes of the two numbers
    return ["No solution found"] # if no match found


# Test cases
print(two_sum([2,7,11,15], 9)) #[0,1]
print(two_sum([3,2,4,7,9], 6)) #[1,2]
print(two_sum([1,3,5,7,9], 16) == [3, 4]) #True
print(two_sum([1,1,2,3], 2) == [0,1]) # True
print(two_sum([-1,-2,-3,-4,-5], -8) == [2,4]) # True


# Time Complexity: O(n^2), because 2 loops (nested loop), n is the length of the lsit nums
# Space Complexity: 0(1), no extra space is used

# Optimal Approach: Using a Dictionary
'''
To solve this problem I am using a dictionary (hash map) approach. 
Instead of checking every pair of numbers, I can store each number I have seen so far in a dictionary
(where Key is the number/element and Value is its index) and then check if the "difference" (what i
need to reach the target) already exists.

How it works:
1. I create/initialize an empty dictionary called `prev_val` to store the numbers I have seen so far along with their indexes.
2. I loop through the list once using single `for loop` with `enumerate()` to get both the index and element.
3. For each current number/element/item, I calculate what number I would need to add to it to reach the target 
   (this is the "diff = target - elem")
4. I check if this needed number (diff) is already exists in my dictionary
5. If it exists, I found my answer. I will return the index of the diff (complement) ans the index from dictionary.
6. If it doesnot exist, I will add the current element and its index in the dictionary for future lookups. 
7. I continue will continue until I find the answer.

Good thing about this approach is I only need to go through the list once (sinlge loop), and checking if element exists in the 
dictionary takes constant time i.e O(1).

Since the problem guarantees exactly one solution exists, I can return immediatley when i find the matching pair.
'''

def two_sum_optimal(nums, target):
    prev_elem = {} # Dict to store previous elements (key) and its index (value)
    for idx, elem in enumerate(nums):
        diff = target - elem # cal diff needed to reach target
        if diff in prev_elem:
            return[prev_elem[diff], idx] # if diff exists in dict, return its index and current index
        prev_elem[elem] = idx # if diff does not exist, add current element and its index to dict
    return ["No answer found"]  

# Test cases
print(two_sum_optimal([2,7,11,15], 9)) #[0,1]
print(two_sum_optimal([3,2,4,7,9], 6)) #[1,2]
print(two_sum_optimal([1,3,5,7,9], 16) == [3, 4]) #True
print(two_sum_optimal([1,1,2,3], 2) == [0,1]) # True
print(two_sum_optimal([-1,-2,-3,-4,-5], -8) == [2,4]) # True

# Time Complexity: O(n), where n is the length of the list nums, because we are going through the list once.
# Space Complexity: O(n), where n is the number of unique elements in the list nums, because we are storing them in a dictionary.