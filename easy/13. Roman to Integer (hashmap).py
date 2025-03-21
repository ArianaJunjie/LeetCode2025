class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I":1, "V":5, "X": 10, "L":50, "C": 100, "D":500, "M": 1000, 
        "IV": 4, "IX": 9, "XL": 40, "XC":90, "CD":400, "CM": 900}
        val = 0
        i = 0 
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in hashmap:
                val += hashmap[s[i:i+2]]
                i += 2  
            else:
                val += hashmap[s[i]]  
                i += 1  
        return val

solution = Solution()
result = solution.romanToInt("IX") 
print(result)  