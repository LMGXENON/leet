class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in hashMap:
                return [hashMap[difference], i]

            hashMap[num] = i
