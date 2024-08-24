arr1 = [-7,8]
arr2 = [-8,-3,8]
join = []
i = j = 0 
while i < len(arr1) and j < len(arr2) :
    if arr1[i] <= arr2[j] :
        if len(join) > 0 and arr1[i] == join[len(join)-1] :
            i+=1
            continue   
        join.append(arr1[i])
        i+=1
    else :
        if len(join) > 0 and arr2[j] == join[len(join)-1] :
            j+=1
            continue  
        join.append(arr2[j])
        j+=1 
while i < len(arr1) :
    if arr1[i] == join[len(join)-1] :
        i+=1
        continue
    join.append(arr1[i])
    i+=1
while j < len(arr2) :
    if arr2[j] == join[len(join)-1] :
        j+=1
        continue 
    join.append(arr2[j])
    j+=1

print(join)