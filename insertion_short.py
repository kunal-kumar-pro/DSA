arr = [9,14,15,12,6,8,13]
# for i in range(len(arr)):
#     j = i
#     while j > 0 and arr[j-1] > arr[j] :     
#         arr[j-1],arr[j] = arr[j],arr[j-1]
#         j -= 1
# print(arr)


def insertion_sort (arr,l):
    if l <= 0 :
        return
    swap(arr,l-1)
    insertion_sort(arr,l-1)

def swap (arr, point) :
    val = arr[point]
    while point <= len(arr) - 2 and val > arr[point + 1] :
        arr[point] = arr[point+1] 
        point += 1
    arr[point] = val




insertion_sort(arr,len(arr))
print(arr)