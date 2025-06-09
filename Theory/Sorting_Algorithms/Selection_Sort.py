def Selection_sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i,len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]


arr = [2,3,6,9,7]
Selection_sort(arr)
print(arr)


# Time Complexity -- O(n^2)
# Space Complexity -- O(1)