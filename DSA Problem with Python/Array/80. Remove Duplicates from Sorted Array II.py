class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return 2
        i = 2
        for j in range(2,len(nums)):
            if i<2 or nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i+=1
        return i
        
