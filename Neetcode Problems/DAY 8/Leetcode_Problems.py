#####   219. Contains Duplicate II   #####

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if abs(i-dic[nums[i]])<=k:
                    return True
                else:
                    dic[nums[i]] = i
        return False

# Time Complexity -- O(n)
# Space Comeplexirty -- O(n)   



#####   121. Best Time to Buy and Sell Stock   #####

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices :
            if price < min_price :
                min_price = price
            else:
                max_profit = max(max_profit , price - min_price) 
        return max_profit       

# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   3. Longest Substring Without Repeating Characters   #####

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = set()
        left = 0
        right = 0
        max_length = 0
        while right < len(s):
            if s[right] not in s1:
                s1.add(s[right])
                max_length = max(max_length,right-left+1)
            else:
                while s[right] in s1:
                    s1.remove(s[left])
                    left += 1
                s1.add(s[right])
            right += 1
        return max_length

# Time Complexity -- O(n)
# Space Complexity -- O(n)



#####   209. Minimum Size Subarray Sum   #####

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_length = float('inf')
        s = 0
        while right < len(nums):
            s += nums[right]
            if s >= target:
                while s >= target and left < len(nums):
                    min_length = min(min_length,right-left+1)
                    s -= nums[left]
                    left += 1

            right += 1    
        if min_length == float('inf'):
            return 0
        else:
            return min_length
        
# Time Complexity -- O(n)
# Space Complexity -- O(1)  