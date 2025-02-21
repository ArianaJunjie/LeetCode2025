class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits_out = digits
        if digits_out[i] != 9:
            digits_out[i] += 1
            return digits_out
        else:
            while i >= 0 and digits_out[i] == 9:
                digits_out[i] = 0
                i -= 1
            if i == -1:
                digits_out.insert(0, 1)
            else:
                digits_out[i] += 1 
            return digits_out