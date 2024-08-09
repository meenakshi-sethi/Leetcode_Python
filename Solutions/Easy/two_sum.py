# Two Sum 
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
            

# print(two_sum([2, 7, 11, 15], 9 ))  # Output: [0, 1], 
# print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
# print(two_sum([3, 3], 6))          # Output: [0, 1]


def twoSum(nums, target):
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i num1 + num2 == target:
                return i, j

print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twosum([3, 2, 4], 6))       # Output: [1, 2]
print(twosum([3, 3], 6))          # Output: [0, 1]
