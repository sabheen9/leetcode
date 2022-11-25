class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_num=list(set(nums))
        for i in range(len(set_num)):
            if nums.count(set_num[i])==1:
                return set_num[i]
            