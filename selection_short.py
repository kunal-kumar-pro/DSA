arr = [4,1,3,9,7]
for i in range(len(arr)-1) :
    min = i
    for j in range(i,len(arr)):
        if arr[j] < arr[min] :
            min = j
    arr[i],arr[min] = arr[min],arr[i]
print(arr)