from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Convert to set to remove duplicates (not in order)
        unique_nums = sorted(set(nums))

        #place unique elements back in the original list up to their count
        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]

        return len(unique_nums)
    
# Example usage:
sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(nums)
print(k) # Output: 5
print(nums[:k]) # Output : [0,1,2,3,4]
