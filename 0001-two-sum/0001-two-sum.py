class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[num] = i
            
           