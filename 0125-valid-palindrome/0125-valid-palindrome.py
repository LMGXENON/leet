class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False
