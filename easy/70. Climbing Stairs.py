class Solution:
    def climbStairs(self, n: int) -> int:
        ## fibonacci ###
        if n == 1:
            return 1
        if n == 2:
            return 2
        fn2 = 1
        fn3 = 2
        i = 3
        fn = 0
        while i <= n:
            fn = fn2 + fn3
            fn2 = fn3
            fn3 = fn
            i += 1
        return fn
            

        
        
        