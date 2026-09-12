class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        
        for i in range(1, len(strs)):
            while not strs[i].startswith(common):
                common = common[:-1]
                if common == "":
                    return ""
        
        return common