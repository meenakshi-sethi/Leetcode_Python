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