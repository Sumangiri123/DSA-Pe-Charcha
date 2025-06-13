#####   912. Sort an Array   #####

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        self.sortArray(left)
        self.sortArray(right)
        return self.merge_array(nums,left,right)


    def merge_array(self,nums,left,right):
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
         
        return nums

# Time Complexity - O(n * log n)
# Space Complexity -- O(1)



#####   75. Sort Colors   #####

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums)<=1:
            return 
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        self.sortColors(left)
        self.sortColors(right)
        self.merge_array(nums,left,right)


    def merge_array(self,nums,left,right):
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
         

# Time Complexity - O(n * log n)
# Space Complexity -- O(1)



#####   912. Sort an Array   #####

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for key in dic:
            if dic[key] > len(nums)/2:
                return key
            
# Time Complexity -- O(n)
# Space Complexity -- O(1)
# Optimise Code Using Moore's Voting Algorithm  



#####   229. Majority Element II   #####

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for key in dic:
            if dic[key] > len(nums)/3:
                result.append(key)
        return result

# Time Complexity -- O(n)
# Space Complexity -- O(n)
# Look for more optimised Code



#####   14. Longest Common Prefix   #####

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i] :
                    return res
            res += strs[0][i]
        return res
        
# n = number of strings in strs
# m = length of the shortest string in strs        
# Time complexity: O(n × m)
# Space complexity: O(m)
# Look for optimised Approach - Sort the array gives first and last as the two most indifferent Words and comparing the first and last Strings
# gives the Longest common prefix - Time Complexity -- O(n*log n)



#####   49. Group Anagrams   #####

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low = -1
        for i in range(len(nums)):
            if nums[i] != val:
                low += 1
                nums[low] = nums[i]   
        return low+1
                
# Time Complexity -- O(n)
# Space Complexity -- O(1)
