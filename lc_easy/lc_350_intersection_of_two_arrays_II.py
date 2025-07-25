#https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Approach 1 - Double loop comparing manually - Brute force
'''
1. Create an empty list result
2. Loop throug nums1 (outer loop) using for loop
3. For each element i in nums1, loop through nums2_copy (inner loop - for loop)
4. if i == j (j is an element from nums2_copy), it means a match is found:
   - append i to result
   - remove j from nums2_copy
   - break the inner loop so that we don't match the same i multiple times
5. After both loops complete, return result

Advantage
- Gives full control over how comparisons and removal are handled
- makes logic easier to trace/debug for beginners

Time Complexity: O(n*m) - nested loop (can be slow for large input)
Space complexity: O(min(n,m)) for result list and the copy of nums2.

'''

def intersect(nums1, nums2):
    result = [] # to store the common elements

    nums2_copy = nums2.copy()

    for i in nums1:
        for j in nums2_copy:
            if i == j: #checking for quality
                result.append(i) # add to the reuslt
                nums2_copy.remove(j) #remove j so its not used again
                break # exit inner loop after a match is found
    return result

#Testcases
print("solution from intersect")
print(intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]  - Basic intersection
print(intersect([4,9,5], [9,4,9,8,4]))  # Output: [4, 9] or [9, 4] - Different Lengths
print(intersect([1, 2, 3], [4, 5, 6]))  # Output: [] - No Intersection
print(intersect([1, 1, 1], [1, 1, 1]))  # Output: [1, 1, 1] - All Elements Intersect
print(intersect([1, 2, 2, 3], [2]))  # Output: [2] - Duplicate in One, Single in Other


# Approach 2 - Single loop using in operator - Brute force
'''
1. Create an empty list `result` to store the intersection.
2. Make a copy of nums2 so we don't modify the original input.
3. Loop through nums1 using a sinlge for loop
4. For each element i in nums1, check if it exists in nums2_copy using `in`.
5. If yes:
   - append to result
   - remove that element from nums2_copy
6. Return result list/array

Advantage
- simpler and more readable than nested loops.

Limitation:
- The `in` operator does a linear search under the hood, so still O(n*m) in the worst case. 

Time Complexity: O(n*m) - because `in` and `remove` are both O(m) 
Space complexity: O(min(n,m)) for result list and the copy of nums2.

'''


def intersect1(nums1, nums2):
    result = [] # empty list to store elements apperaing in both the list due to intersection

    nums2_copy = nums2.copy() # so we dont modify original input    
    for i in nums1: # loop through each element in nums1
        if i in nums2_copy: # check if its present in nums2_copy
            result.append(i) # add to result
            nums2_copy.remove(i) # remove one occurence so it doesn't match again
    
    return result # return the final list


# Test cases
print("solution from intersect1")
print(intersect1([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]  - Basic intersection
print(intersect1([4,9,5], [9,4,9,8,4]))  # Output: [4, 9] or [9, 4] - Different Lengths
print(intersect1([1, 2, 3], [4, 5, 6]))  # Output: [] - No Intersection
print(intersect1([1, 1, 1], [1, 1, 1]))  # Output: [1, 1, 1] - All Elements Intersect
print(intersect1([1, 2, 2, 3], [2]))  # Output: [2] - Duplicate in One, Single in Other


# Hash Map using collections.Counter
'''
Idea/Intution here is to
1. Count the frequency of elements in one array using `Counter`. `Counter` counts how many times each element apprears
2. For each element in the other array, check if it's in the counter
3. If yes, append and decrease count
We only care about elements present in both arrays and for each such element we take the minimum count(to avoid overcounting)

-- The hash map approach (i.e., Counter) is best for unsorted input.

Counter is a subclass of dict from Python's collections module. It is specifically designed to count frequencies of elements in an iterable (like a list, string, etc.).

'''

from collections import Counter

def intersect2(nums1, nums2):
    cnt1 = Counter(nums1) # Count frequency in nums1
    cnt2 = Counter(nums2) # Count frequency in nums2

    result = []

    # loop through cnt1 keys and check if present in cnt2
    for num in cnt1:
        if num in cnt2:
            result.extend([num]*min(cnt1[num], cnt2[num])) # add the element min(cnt1[num], cnt2[num]) times

    return result 

# Test cases
print("solution from intersect2")
print(intersect2([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]  - Basic intersection
print(intersect2([4,9,5], [9,4,9,8,4]))  # Output: [4, 9] or [9, 4] - Different Lengths
print(intersect2([1, 2, 3], [4, 5, 6]))  # Output: [] - No Intersection
print(intersect2([1, 1, 1], [1, 1, 1]))  # Output: [1, 1, 1] - All Elements Intersect
print(intersect2([1, 2, 2, 3], [2]))  # Output: [2] - Duplicate in One, Single in Other


# Hash map without counter using Manual Dictionary frequency map 
'''
Idea/Intution here is to
1. Use a plain dictionary (dict) to count elements in one array.
2. Iterate over the second array and reduce the count if the element exists
'''

def intersect3(nums1, nums2):
    count = {}
    for num in nums1:
        count[num] = count.get(num, 0) + 1
    
    result = []

    for num in nums2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1
    
    return result
    

# Test cases
print("solution from intersect3")
print(intersect3([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]  - Basic intersection
print(intersect3([4,9,5], [9,4,9,8,4]))  # Output: [4, 9] or [9, 4] - Different Lengths
print(intersect3([1, 2, 3], [4, 5, 6]))  # Output: [] - No Intersection
print(intersect3([1, 1, 1], [1, 1, 1]))  # Output: [1, 1, 1] - All Elements Intersect
print(intersect3([1, 2, 2, 3], [2]))  # Output: [2] - Duplicate in One, Single in Other