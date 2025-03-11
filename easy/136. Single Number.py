class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            if i not in lst:
                lst.append(i)
            else:
                lst.remove(i)
        return lst[0]
        
    
# Concept of XOR (run time much faster):
#Self-inverse: x ^ x = 0. So if a number appears twice, it will cancel out.
#Commutative: The order doesn't matter: a ^ b = b ^ a.
#Associative: The grouping doesn't matter: (a ^ b) ^ c = a ^ (b ^ c)

# e.g Consider the array nums = [4, 1, 2, 1, 2]:
#Initial: uniqNum = 0
#uniqNum = 0 ^ 4 = 4
#uniqNum = 4 ^ 1 = 5
#uniqNum = 5 ^ 2 = 7
#uniqNum = 7 ^ 1 = 6
#uniqNum = 6 ^ 2 = 4 (final result)

#        # Initialize the unique number...
#        uniqNum = 0;
#        # TRaverse all elements through the loop...
#        for idx in nums:
#            # Concept of XOR...
#            uniqNum ^= idx;
#       return uniqNum;       # Return the unique number...