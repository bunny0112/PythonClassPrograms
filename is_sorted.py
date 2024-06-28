def is_sorted(arr):
    for i in range(0,len(arr)):
        if arr[i]<arr[i+1]:
            continue
        else
            return False
    return True

arr=[2,4,6,2,3,9]
arr.sort()
print(is_sorted(arr))