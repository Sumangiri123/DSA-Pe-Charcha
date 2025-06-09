def merge_sort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left) # O(log n)
    merge_sort(right) # O(log n)
    merge_array(arr,left,right) # O(n)


def merge_array(arr,left_arr,right_arr):
    i = 0
    j = 0
    k = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    
arr = [5,4,3,2,1]
merge_sort(arr)
print(arr)

# Time Complexity -- O(n*log n)
# Space Complecity -- O(n)



