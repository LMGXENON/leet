class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        reversed = str(abs(x))[::-1]
        if x < 0:
            result = int(reversed) * -1
        else:
            result = int(reversed)

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result