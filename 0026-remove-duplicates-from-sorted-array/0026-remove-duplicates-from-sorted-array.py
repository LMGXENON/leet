class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cleaned = list(dict.fromkeys(nums))

        for i in range(len(cleaned)):
            nums[i] = cleaned[i]

        return len(cleaned)