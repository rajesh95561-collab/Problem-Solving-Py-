def maxConsecutiveOnes1(arr, k):
    window = []
    max_consecutiveOnes = 0
    zero_count = 0
    left = 0

    for right in range(len(arr)):
        window.append(arr[right])
        if arr[right] == 0:
            zero_count += 1
        # shrink window if zeros exceed k
        while zero_count > k:
            if window[0] == 0:
                zero_count -= 1
            window.pop(0)
            left += 1
        max_consecutiveOnes = max(max_consecutiveOnes, len(window))
    return max_consecutiveOnes

def maxConsecutiveOnes2(nums, k):
    l = r = 0
    zeroes = 0
    max_len = 0
    while r < len(nums):
        if nums[r] == 0:
            zeroes += 1
        if zeroes > k:
            if nums[l] == 0:
                zeroes -= 1
            l += 1
        if zeroes <= k:
            max_len = max(max_len, r - l + 1)
        r += 1
    return max_len


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(maxConsecutiveOnes1(nums, k))
print(maxConsecutiveOnes2(nums, k))