def Search(arr, low, high, k):
    if low > high:  
        return -1
    mid = (low + high) // 2
    if arr[mid] == k:
        return 1
    elif arr[mid] < k:
        return Search(arr, mid + 1, high, k)
    else:
        return Search(arr, low, mid - 1, k)

arr = [1, 2, 3, 4, 5, 6]
a = Search(arr, 0, len(arr) - 1, 6)
print(a)
