#####   153. Find Minimum in Rotated Sorted Array   #####

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 1
        arr = nums
        mini = 0
        while low <= high :
            mid = low + (high-low)//2
            if arr[mid] < arr[mini]:
                mini = mid
            elif nums[mid] < nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        return arr[mini]

# Time Complexity : O(log n)
# Space Complexity : O(1)



#####   33. Search in Rotated Sorted Array   #####

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1
        arr = nums
        while low <= high :
            mid = low + (high-low)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < nums[high]: # Sorted Part
                if arr[mid] <= target and arr[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:                       # Unsorted Part
                if arr[mid] >= target and arr[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
        
# Time Complexity : O(log n)
# Space Complexity : O(1)


#####   81. Search in Rotated Sorted Array II   #####

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0 
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True
            if nums[mid] == nums[high]:
                high -= 1
            elif nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False

# Time Complexity -- O(n) in Worst Case and O(log n) in average Case
# Space Complexity -- O(1)


