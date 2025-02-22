class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        a_decimal = 0
        b_decimal = 0
        while i>= 0:
            a_decimal = a_decimal + (int(a[i]) * 2**(len(a) -1 - i)) 
            i -= 1
        while j>= 0:
            b_decimal = b_decimal + (int(b[j]) * 2**(len(b) -1- j))
            j -= 1    
        sum_decimal = a_decimal + b_decimal
        
        # Much More Efficient
        # sum_decimal = int(a,2) + int(b,2)
        string = ""

        if sum_decimal == 0:
            return "0"
        while sum_decimal > 0 :
            remainder = str(sum_decimal%2)
            sum_decimal = sum_decimal//2
            string = remainder + string
        return string

        