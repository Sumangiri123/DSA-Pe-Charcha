def Insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        key = arr[j+1]
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [5,4,3,2,1]
Insertion_sort(arr)
print(arr)


# Time Complexity -- O(n^2)
# Space Complexity --  O(1)