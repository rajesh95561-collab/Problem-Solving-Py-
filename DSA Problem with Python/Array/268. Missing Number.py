class Solution:
    def missingNumber(self, nums):
        # for i in range(len(nums)+1):
        #     if i in nums:
        #         continue
        #     else:
        #         return i

        # method 2
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)

nums = [3,0,1]
solution = Solution()
print(solution.missingNumber(nums))