#Brute Force
def maxSum(copy_arr,copy_k):
    max_sum = 0
    for i in range(len(copy_arr)-k+1):
        curr_sum = sum(copy_arr[i:i+k])
        max_sum = max(max_sum,curr_sum)
    return max_sum

arr = [2,1,5,1,3,2]
k = 3
print(maxSum(arr,k))

#Sliding Window
def maxSum(copy_arr, copy_k):
    n = len(copy_arr)
    if n < copy_k:
        return None
    #store first window value
    window_sum = sum(copy_arr[:copy_k])
    max_sum = window_sum
    #Next Slide the window
    for i in range(copy_k, n):
        window_sum += copy_arr[i] - copy_arr[i - copy_k]
        max_sum = max(max_sum,window_sum)
    return max_sum

arr = [2,1,5,1,3,2]
k = 3
print(maxSum(arr,k))

# Brute Force: recalculates sums → O(n.k).
# Sliding window version: updates sums incrementally → O(n).
