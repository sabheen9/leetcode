class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(min(nums),len(nums)+1,1):
            if(i not in nums):
                return i
        return 0
        
        