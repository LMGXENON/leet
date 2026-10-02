class Solution:
    def mySqrt(self, x: int) -> int:

        sqrt = 0

        while (sqrt + 1) * (sqrt + 1) <= x:
            sqrt += 1
        
        return sqrt