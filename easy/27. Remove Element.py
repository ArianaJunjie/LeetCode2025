class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if i == 0 and nums[i] != val:
                j += 1
            elif nums[i] != val:
                 nums[j] = nums[i] 
                 j += 1
        return j
    
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 2.
#It does not matter what you leave beyond the returned k (hence they are underscores).
