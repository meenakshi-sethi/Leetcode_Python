# LC 88 Mergered Sorted Array

# Approach 1: Append + sort - but violates in place merge. LeetCode usually wants in-place
"""
put nums 2 into the tail of nums1 and then nums1.sort().
"""

# method 1 Slicing

def merge1(nums1, nums2, m, n):
    nums1[m:m+n]= nums2 # to replace the last n zeros of nums1 with the contents of nums2
    nums1.sort()
    print(nums1)

# method 2 by using .extent() method

def merger2(nums1, nums2, m, n):
    # nums1 already has the placeholder 0's at the end so we will first slice away that part
    nums1[m:] = [] # remove trailing 0 placeholders
    nums1.extend(nums2) # appends each element of nums2 individually
    nums1.sort()
    print(nums1)
 


# Three Pointers approach

def merge3(nums1, nums2, m, n):
    # last index nums1
    last = m + n - 1

    #merge in reverse order
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    # fill nums1 with leftover nums2 elements
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last -1


# Test cases 

# Test case runner
def run_tests():
    # 1) Basic case
    nums1 = [1,2,3,0,0,0]; nums2 = [2,5,6]; m, n = 3, 3
    merge1(nums1[:], nums2[:], m, n)   # → [1,2,2,3,5,6]
    merger2(nums1[:], nums2[:], m, n)  # → [1,2,2,3,5,6]
    merge3(nums1[:], nums2[:], m, n)   # → [1,2,2,3,5,6]

    # 2) nums1 has no valid elements (m=0)
    nums1 = [0]; nums2 = [1]; m, n = 0, 1
    merge1(nums1[:], nums2[:], m, n)   # → [1]
    merger2(nums1[:], nums2[:], m, n)  # → [1]
    merge3(nums1[:], nums2[:], m, n)   # → [1]

    # 3) nums2 is empty (n=0)
    nums1 = [1]; nums2 = []; m, n = 1, 0
    merge1(nums1[:], nums2[:], m, n)   # → [1]
    merger2(nums1[:], nums2[:], m, n)  # → [1]
    merge3(nums1[:], nums2[:], m, n)   # → [1]

    # 4) All nums2 elements smaller
    nums1 = [4,5,6,0,0,0]; nums2 = [1,2,3]; m, n = 3, 3
    merge1(nums1[:], nums2[:], m, n)   # → [1,2,3,4,5,6]
    merger2(nums1[:], nums2[:], m, n)  # → [1,2,3,4,5,6]
    merge3(nums1[:], nums2[:], m, n)   # → [1,2,3,4,5,6]

    # 5) All nums2 elements larger
    nums1 = [1,2,3,0,0,0]; nums2 = [4,5,6]; m, n = 3, 3
    merge1(nums1[:], nums2[:], m, n)   # → [1,2,3,4,5,6]
    merger2(nums1[:], nums2[:], m, n)  # → [1,2,3,4,5,6]
    merge3(nums1[:], nums2[:], m, n)   # → [1,2,3,4,5,6]

    # 6) With duplicates
    nums1 = [1,2,2,0,0,0]; nums2 = [2,2,3]; m, n = 3, 3
    merge1(nums1[:], nums2[:], m, n)   # → [1,2,2,2,2,3]
    merger2(nums1[:], nums2[:], m, n)  # → [1,2,2,2,2,3]
    merge3(nums1[:], nums2[:], m, n)   # → [1,2,2,2,2,3]

    # 7) Negative numbers
    nums1 = [-3,-2,-1,0,0,0]; nums2 = [-5,-4,-3]; m, n = 3, 3
    merge1(nums1[:], nums2[:], m, n)   # → [-5,-4,-3,-3,-2,-1]
    merger2(nums1[:], nums2[:], m, n)  # → [-5,-4,-3,-3,-2,-1]
    merge3(nums1[:], nums2[:], m, n)   # → [-5,-4,-3,-3,-2,-1]

run_tests()

