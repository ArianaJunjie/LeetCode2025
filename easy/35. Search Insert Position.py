## solve this question with binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
    
# If nums[mid] < target, we know that the target is in the right half, 
# so we update left to mid + 1 (the first index of the right half).

# If nums[mid] > target, we know the target is in the left half, 
# so we update right to mid - 1 (the last index of the left half).

# By doing this, we reduce the search space by half at each step, 
# making the algorithm efficient with O(log n) time complexity.
