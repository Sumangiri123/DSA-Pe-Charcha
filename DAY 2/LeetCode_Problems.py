#####   69. Sqrt(x)     #####

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low<=high:
            mid = low + (high-low)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans
        
        
# Time Complexity -- O(log n)
# Space Complexity -- O(1)


#####   74. Search a 2D Matrix   #####

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = m*n-1
        while low<=high:
            mid = low + (high-low)//2
            row = mid//n
            col = mid%n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid+1
            else:
                high = mid-1
            
        return False
    

# Time Complexity -- O(log(m*n))
# Space Complexity -- O(1)


#####   875. Koko Eating Bananas   #####

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        prev_hour_taken = 0
        while start<=end:
            mid = start + (end-start)//2
            hours_taken = 0
            for i in range(len(piles)):
                if piles[i]%mid == 0:
                    hours_taken += piles[i]//mid
                else:
                    hours_taken += (piles[i]//mid)+1
            if hours_taken <= h:
                
                end = mid - 1
            else:
                start = mid + 1
        return start

# Time Complexity -- O(n * log n) 
# Space Complexity -- O(1)

