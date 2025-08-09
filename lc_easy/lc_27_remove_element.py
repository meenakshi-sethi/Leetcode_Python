# lec_27_remove_elements

# Two pointer approach

def removeElements(nums, val):
    k = 0 # array length counter (slow pointer)

    for i in range(len(nums)): # scans the array. here i is fast pointer
        if nums[i] != val: # if current number is not eqaul to val 
            nums[k] = nums[i] # place current number at postion k
            k += 1 # moving slow pointer forward
    return k # length of filtered array


# Test Cases

nums1 = [3,2,2,3]
k1 = removeElements(nums1, 3)
print(k1, nums1[:k1])  # 2 [2, 2]

nums2 = [0,1,2,2,3,0,4,2]
k2 = removeElements(nums2, 2)
print(k2, nums2[:k2])  # 5 [0, 1, 3, 0, 4]

nums3 = [1,1,1,1]
k3 = removeElements(nums3, 1)
print(k3, nums3[:k3])  # 0 []


