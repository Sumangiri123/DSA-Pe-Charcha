#####   344. Reverse String  #####

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   125. Valid Palindrome   #####

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for ch in s:
            if ch.isupper():
                ch = ch.lower()
            if ch.isalnum():
                res += ch
            else:
                continue
        left = 0
        right = len(res)-1
        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True

# Time Complexity -- O(n)
# Space Complexity -- O(1)   



#####   1768. Merge Strings Alternately   #####

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            merged.append(word1[i])
            i += 1
        while j < len(word2):
            merged.append(word2[j])
            j += 1
        return ''.join(merged)

# m = len(word1) , n = len(word2)
# Time Complexity -- O(max(m,n))
# Space Complexity -- O(max(m,n))



#####  88. Merge Sorted Array   #####

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        k = m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j>=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   26. Remove Duplicates from Sorted Array   #####

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 0
        count = 1
        while right < len(nums)-1:
            if nums[right] == nums[right+1]:
                right += 1
            else:
                count += 1
                nums[left] = nums[right+1]
                right += 1
                left += 1
        
        return count

# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   167. Two Sum II - Input Array Is Sorted   #####

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] == target:
                res.append(left+1)
                res.append(right+1)
                return res
            elif numbers[left]+numbers[right] > target:
                right -= 1
            else:
                left += 1

# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   11. Container With Most Water   #####

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        while left < right:
            area = (right-left)*min(height[left],height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area,area)
        return max_area

# Time Complexity -- O(n)
# Space Complexity -- O(1)