
def max_average(arr,k):
    n = len(nums)
    window = sum(nums[:k])
    max_avg = window / k
    for i in range(k, n):
        window += nums[i] - nums[i - k]
        max_avg = max(max_avg, window / k)
    return max_avg

nums = [1,12,-5,-6,50,3]
k = 4
print(max_average(nums,k))
