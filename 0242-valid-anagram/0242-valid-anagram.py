class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sortedS = sorted(list(s))
        sortedT = sorted(list(t))

        if sortedS == sortedT:
            return True
        else:
            return False
        