# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# # Example usage:
# arr = [3, 6, 8, 10, 1, 2, 1]
# print("Original array:", arr)
# sorted_arr = quicksort(arr)
# print("Sorted array:", sorted_arr)

# def quick_sort(arr, low, high):
#     def partition(arr, low, high):
#         pivot = arr[low]
#         i = low + 1
#         for j in range(low + 1, high + 1):
#             if arr[j] < pivot:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 i += 1
#         arr[low], arr[i - 1] = arr[i - 1], arr[low]
#         return i - 1

#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)

# Example usage

def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[low]
        i = low + 1
        j = high
        
        while True:
            while i <= high and arr[i] <= pivot:
                i += 1
            while j >= low and arr[j] > pivot:
                j -= 1
            
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        
        quick_sort(arr, low, j - 1)
        quick_sort(arr, j + 1, high)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    n = len(arr)
    print("Unsorted array:", arr)
    quick_sort(arr, 0, n - 1)
    print("Sorted array:", arr)
