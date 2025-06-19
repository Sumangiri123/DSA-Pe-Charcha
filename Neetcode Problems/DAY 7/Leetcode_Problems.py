#####   680. Valid Palindrome II   #####

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left]!=s[right]:
                return self.check_palindrome(s,left+1,right) or self.check_palindrome(s,left,right-1)
            left += 1
            right -= 1
        return True


    def check_palindrome(self,s,left,right):
        while left < right:
            if s[left]!=s[right]:
                return False
            left += 1
            right -= 1
        return True 
        
# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   15. 3Sum   #####

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    triplet = tuple([nums[i], nums[left], nums[right]])
                    s.add(triplet)
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        res = [list(t) for t in s]
        return res

# Time Complexity -- O(n^2)
# Space Complexity -- O(k) where k<=n^2



#####   18. 4Sum   #####

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s = set()
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        triplet = tuple([nums[i],nums[j] ,nums[left], nums[right]])
                        s.add(triplet)
                        left += 1
                        right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
            
        res = [list(t) for t in s]
        return res

# Time Complexity -- O(n^3)
# Space Complexity -- O(k) where k<=n^2 


#####  189. Rotate Array   #####

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   881. Boats to Save People   #####

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # TC : O(n*log n)
        boats_required = 0
        left = 0
        right = len(people)-1
        while left <= right:
            if people[right] + people[left] > limit:
                boats_required += 1
                right -= 1
            else:
                boats_required += 1
                left += 1
                right -= 1

        return boats_required

# Approach -- Sorting + Two Pointer                 
# Time Complexity -- O(n*log n)
# Space Complexity -- O(1)






