class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         
        k = 0

        for current_value in nums:
            if current_value != val:
                nums[k] = current_value
                k += 1

        return k
        