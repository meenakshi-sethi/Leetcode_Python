from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2 #finding the middle index

            if nums[mid] == target:
                return mid  # Target found at index `mid`
            elif nums[mid] < target:
                left = mid + 1 # Search in the right half
            else:
                right = mid - 1 # Search in the left half
        return left # Return the insertion position

# Example usage:
print(Solution().searchInsert([1, 3, 5, 6], 5))  # Output: 2
print(Solution().searchInsert([1, 3, 5, 6], 2))  # Output: 1
print(Solution().searchInsert([1, 3, 5, 6], 7))  # Output: 4
print(Solution().searchInsert([1, 3, 5, 6], 0))  # Output: 0
print(Solution().searchInsert([1], 1))           # Output: 0