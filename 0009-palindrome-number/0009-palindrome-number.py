class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse = s[::-1]
        
        if s == reverse:
            return True
        else:
            return False