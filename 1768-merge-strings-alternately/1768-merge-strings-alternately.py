class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

       # Loop up to the length of the longest word
        for i in range(max(len(word1), len(word2))):
            # If i is still inside word1's length, grab its letter
            if i < len(word1):
                result.append(word1[i])
            # If i is still inside word2's length, grab its letter
            if i < len(word2):
                result.append(word2[i])
                
        # Stitch all the pieces back together into one string
        return "".join(result)
            