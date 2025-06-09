def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]



arr = [5,4,1,2,9,8,3,7]
bubble_sort(arr)
print(arr)

# Time Complexity -- O(n^2)
# Space Complexity -- O(1)



# Modified Bubble Sort -- Aim is to stop iterating as when sorted array is obtained(Helpful for sorted or nearly sorted array)

def modified_bubble_sort(arr): 
    for i in range(len(arr)-1,0,-1):
        flag = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                flag = 1
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if flag == 0:
            break


arr = [5,4,1,2,9,8,3,7]
modified_bubble_sort(arr)
print(arr)

# Time Complexity and Space Complexity is similar to above  