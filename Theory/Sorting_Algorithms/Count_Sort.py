# Used to Sort Array of Numbers 
# Numbers Should not be of high value

# Concept : 

# First Find max_element -- create an array of size max_element+1 and intialize all elements with 0 --
# Iterate Through the original array and treat its element as index of new array -- Increment by 1 at the respective position --
# find predix sum - create an output array -- new array index is the element and its element it its position in the sorted array

def count_sort(arr):
    max_element = max(arr)
    new_arr = [0]*(max_element+1)
    for num in arr:
        new_arr[num] += 1
    for i in range(1,len(new_arr)):
        new_arr[i] += new_arr[i-1]
    output_arr = [0]*len(arr)
    for i in range(len(arr)):
        output_arr[new_arr[arr[i]]-1] = arr[i]
        new_arr[arr[i]] -= 1
    return output_arr


arr = [1,6,8,9,11,7]
print(count_sort(arr))


# Time Complexity -- O(n)
# Space Complexity -- O(n)