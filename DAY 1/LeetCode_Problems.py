##### 704. Binary Search ########

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1
    
# Time Complexity - O(log n)
# Spcae Complexity - O(1)



##### 35. Search Insert Position  ######

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        if nums[mid] < target:
            return mid+1
        else:
            return mid

# Time Complexity - O(log n)
# Space Complexity - O(1)



####### 374. Guess Number Higher or Lower    ###########

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low<=high:
            mid = low + (high-low)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                low = mid+1
            else:
                high = mid-1


# Time Complexity - O(log n)
# Space Complexity - O(1)



######### 168. Excel Sheet Column Title   #########

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            ch = chr(65 + columnNumber % 26)
            res = ch + res 
            columnNumber = columnNumber//26

        return res

# Time Complexity - O(log n)
# Spcae Complexity - O(n)