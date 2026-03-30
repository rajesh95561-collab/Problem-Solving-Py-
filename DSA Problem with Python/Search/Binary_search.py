def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid+1, high, target)
    else:
        return binary_search(arr, low, mid-1, target)

# Input
input_arr = []
print("Enter 10 integer elements separated by space")
for _ in range(10):
    input_arr.append(int(input()))

print(f"Entered Array: {input_arr}")

# Work on a sorted copy
sorted_arr = sorted(input_arr)
print(f"Sorted Array: {sorted_arr}")

given_target = int(input("Enter target number: "))
found = binary_search(sorted_arr, 0, len(sorted_arr) - 1, given_target)

if found != -1:
    # Map back to original index
    original_index = input_arr.index(sorted_arr[found])
    print(f"{given_target} found at index {original_index} in original array")
else:
    print(f"{given_target} not found")
