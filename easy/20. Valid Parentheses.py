class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(": ")", "{": "}", "[": "]"}
        lst = []
        for i in range(len(s)):
            if s[i] in hashmap.keys():
                lst.append(s[i])
            elif s[i] in hashmap.values():
                if not lst:
                    return False
                pop_elm = lst.pop()
                if hashmap[pop_elm] != s[i]:
                    return False
        return len(lst) == 0

        