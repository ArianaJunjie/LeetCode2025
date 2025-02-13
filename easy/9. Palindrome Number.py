class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        str_y = str_x[::-1]
        
        if str_x == str_y:
            return True
        else:
            return False

solution = Solution()
result = solution.isPalindrome(121) 
print(result)  


        