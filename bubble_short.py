arr = [24,18,38,43,14,40,1,54]
# arr.sort()
# for i in range (1,len(arr)):
#     swap = 0
#     for j in range(1,len(arr)-i+1) :
#         if arr[j-1] > arr[j] :
#             arr[j-1],arr[j] = arr[j],arr[j-1]
#             swap = 1
#     if swap == 0:
#         break
# print(arr)

# i = len(arr) - 1 
# while(i>= 1):
#     swap = 0
#     for j in range(i-1):
#         if arr[j] > arr[j+1] :
#             arr[j] ,arr[j+1] = arr[j+1] , arr[j]
#             swap = 1
#     if swap != 1:
#         break
#     i -=1
# print(arr)

def bubble_sort(arr, high):
    if high <= 0:
        return
    else:
        swap(arr, high)
        bubble_sort(arr, high - 1)

def swap(arr, high):
    if high <= 0:
        return
    if arr[high] < arr[high - 1]:
        arr[high - 1], arr[high] = arr[high], arr[high - 1]
        swap(arr, high - 1)

bubble_sort(arr,len(arr)-1)
print(arr)