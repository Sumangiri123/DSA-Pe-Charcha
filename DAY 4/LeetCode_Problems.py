#####   1011. Capacity To Ship Packages Within D Days   #####

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        result = 0
        while low <= high:
            capacity = low + (high-low)//2
            current = 0
            days_taken = 1
            for weight in weights:
                if current + weight > capacity:
                    days_taken += 1
                    current = 0
                current += weight
            
            if days_taken <= days:
                result = capacity
                high = capacity-1
            else:
                low = capacity + 1

        return result
            
# Time Complexity -- O(n*log n)
# Space Complexity -- O(1)

        

#####   981. Time Based Key-Value Store   #####

class TimeMap:

    def __init__(self):
        self.values = []
        self.dict = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.values.append([value,timestamp])
            self.dict[key] = self.values
            self.values = []
        else:
            self.dict[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return "" 
        start = 0
        end = len(self.dict[key])-1
        arr = self.dict[key]
        result = ""
        while start<=end:
            mid = start + (end-start)//2
            if arr[mid][-1] == timestamp:
                return arr[mid][0]
            elif arr[mid][-1] < timestamp:
                result = arr[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        return result


# Time Complexity -- O(log n)
# Space Complexity -- O(n)

# This Time and Space Complexity is according to get() function



#####   136. Single Number   #####

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            num ^= nums[i]
        return num
        
    # Time Complexity -- O(n)
    # Space Complexity -- O(1)



#####   191. Number of 1 Bits   #####

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            lsb = n & 1
            if lsb == 1:
                count += 1
            n = n>>1
        return count

# Time Complexity -- O(log n)
# Space Complexity -- O(1)



#####   1929. Concatenation of Array   #####

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        n = len(nums)
        for i in range(len(nums)):
            ans[i] = ans[i+n] = nums[i]
        return ans

# Time Complexity -- O(n)
# Space Complexity -- O(n)



#####   217. Contains Duplicate   #####

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])
        if len(nums) == len(s):
            return False
        return True
        
# Time Complexity -- O(n)
# Space Complexity -- O(n)



#####   242. Valid Anagram   #####

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        for i in s:
            if i not in dict_1.keys():
                dict_1[i] = 1
            else:
                dict_1[i] += 1
        for j in t:
            if j not in dict_2.keys():
                dict_2[j] = 1
            else:
                dict_2[j] += 1
        return dict_1 == dict_2

# Time Complexity -- O(n) where n is the length of the string
# Space Complexity -- O(n)



#####   1. Two Sum   #####

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in dic:
                dic[nums[i]] = i
            else:
                result.append(dic[complement])
                result.append(i)
                return result
                     
        
# Time Complexity -- O(n)
# Space Complexity -- O(n)