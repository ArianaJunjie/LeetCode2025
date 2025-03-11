class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        # Alternative 1: s = ''.join(c.lower() for c in s if c.isalnum())
        # A2: regular expression: s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        # return s == s[::-1]
        while i <= j:
            if s[i] == '' or not s[i].isalnum():
                i += 1
            elif s[j] == '' or not s[j].isalnum():
                j -= 1
            elif s[i] != s[j]:
                return False
            elif s[i] == s[j]:
                i += 1
                j -= 1
        return True                
            
            
