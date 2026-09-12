class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)

        if n == 3:
            for i in range(n):
                if i == 1:
                    return merged[i]
        else:
            mid = n // 2
            if n % 2 != 0:
                for i in range(n):
                    if i == mid:
                        return merged[i]
            else:
                first = None
                second = None
                for i in range(n):
                    if i == mid - 1:
                        first = merged[i]
                    if i == mid:
                        second = merged[i]
                return (first + second) / 2