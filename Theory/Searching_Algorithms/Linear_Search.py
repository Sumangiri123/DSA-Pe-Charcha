def Linear_Search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1,2,3,4,5,6,8]
target = 6
print(Linear_Search(arr,target))


# Time Complexity - O(n)
# Space Complexity - O(1) -- Constant Space Complexity or Inplace Complexity
