# def merge_short(arr) :
#     if len(arr) <= 1 :
#         return arr
#     mid = len(arr) // 2
#     left_half = merge_short(arr[:mid])
#     right_half = merge_short(arr[mid:])
#     return merge(left_half,right_half)

# def merge(left_half,right_half) :
#     shorted_array = []
#     i = j = 0
#     while (i < len(left_half) and j < len(right_half) ) :
#         if left_half[i] < right_half[j] :
#             shorted_array.append(left_half[i])
#             i += 1
#         else :
#             shorted_array.append(right_half[j])
#             j += 1
#     shorted_array.extend(left_half[i:])
#     shorted_array.extend(right_half[j:])
#     return shorted_array

# arr = [34,7,23,32,5,62]
# shorted_array = merge_short(arr)
# print(shorted_array)

def merge (arr,low,mid,high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i = j = 0
    k = low
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            arr[k] = left[i]
            k+=1
            i+=1
        else :
            arr[k] = right[j]
            k+=1
            j+=1
    while i < len(left) :
        arr[k] = left[i]
        k+=1
        i+=1
    while j < len(right) :
        arr[k] = right[j]
        k+=1
        j+=1



def merge_Short (arr,low,high) :
    if low >= high :
        return
    mid = (low + high)//2
    merge_Short(arr,low,mid)
    merge_Short(arr,mid+1,high)
    merge(arr,low,mid,high)



arr = [34,7,23,32,5,62]
shorted_array = merge_Short(arr,0,len(arr)-1)
print(arr)