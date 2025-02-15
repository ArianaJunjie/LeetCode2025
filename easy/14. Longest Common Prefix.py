class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]: 
                    ## if it achieves the length of the shortest word or not match, return
                    return strs[0][:i]
        return strs[0]