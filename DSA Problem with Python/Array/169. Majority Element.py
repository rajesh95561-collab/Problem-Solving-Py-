#The middle element (nums[n/2]) will always be the majority element after sorting.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        return nums[int(n/2)]
        
