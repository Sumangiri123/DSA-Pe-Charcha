# Condition to apply Searching on array -- The array must be sorted 

def Binary_Search(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 

# Time Complexity -- O(log n)
# Space Complexity -- O(1)

# Binary Search Using Recursion

def Binary_Search_Recursion(arr,start,end,target):
    if start > end :
        return -1 
    mid = start + (end - start)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target : 
        return Binary_Search_Recursion(arr,mid+1,end,target)
    else:
        return Binary_Search_Recursion(arr,start,mid-1,target)
    
arr = [1,2,3,4,5,6]
target = 2
print(Binary_Search_Recursion(arr,0,len(arr)-1,target))

print(Binary_Search(arr,target))