def linear_Search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

def binary_Search(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1 
        else:
            high = mid-1
    return -1 

def binary_search_recursion(arr,low,high,target):
    if low>high:
        return 
    mid = low + (high-low)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]<target:
        return binary_search_recursion(arr,mid+1,high,target)
    else:
        return binary_search_recursion(arr,low,mid-1,target)
    
def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for  j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def modified_bubble_sort(arr): # To decrease the number of iterations 
    for i in range(len(arr)-1,0,-1):
        flag = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if flag == 0:
            break

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[j+1]
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
def merge_sort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,arr)

def merge(left,right,arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def quick_sort(arr,low,high):
    if low > high:
        return 
    pi = partition(arr,low,high)
    quick_sort(arr,low,pi-1)
    quick_sort(arr,pi+1,high)

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def count_sort(arr):
    max_element = max(arr)
    count_arr = [0]*(max_element+1)
    for num in arr:
        count_arr[num] += 1
    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]
    output_arr = [0]*len(arr)
    for i in range(len(arr)):
        output_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1
    return output_arr



arr = [5,4,1,3,2]

# print(linear_Search(arr,2))

arr1 = [1,2,3,4,5]

# print(binary_Search(arr1,4))

# print(binary_search_recursion(arr1,0,len(arr)-1,4))

# bubble_sort(arr)
# print(arr)

# selection_sort(arr)
# print(arr)

# insertion_sort(arr)
# print(arr)

# arr2 = count_sort(arr)
# print(arr2)

# merge_sort(arr)
# print(arr)

# quick_sort(arr,0,len(arr)-1)
# print(arr)

modified_bubble_sort(arr)
print(arr)