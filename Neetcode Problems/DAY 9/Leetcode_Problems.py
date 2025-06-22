#####  424. Longest Repeating Character Replacement   #####

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        count = defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
            
# Time Complexity -- O(n)
# Space Complexity -- O(1)



#####   567. Permutation in String   #####

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        i = 0
        while i < len(s1):
            if s1[i] not in hashmap1:
                hashmap1[s1[i]] = 1
            else:
                hashmap1[s1[i]] += 1
            i += 1
        j = 0
        while j <= (len(s2)-len(s1)):
            temp = s2[j:j+len(s1)]
            for ch in temp:
                if ch not in hashmap2 :
                    hashmap2[ch] = 1
                else:
                    hashmap2[ch] += 1
            if hashmap1 == hashmap2:
                return True
            hashmap2 = {}
            j += 1

        return False 

# m = len(s1)
# n = len(s2)
# Time Complexity: O(n * m)
# Space Complexity: O(m)



#####   658. Find K Closest Elements   #####

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k  

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

# Time Complexity -- O(log(n - k) + k)
# Space Complexity: O(1)