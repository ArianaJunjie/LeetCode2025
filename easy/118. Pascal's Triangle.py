class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        lst = [[1], [1,1]]
        for i in range(2, numRows):
            lst_i = []
            lst_i.append(1)
            for j in range(len(lst[i-1])-1):
                lst_i.append(lst[i-1][j] + lst[i-1][j+1])
            lst_i.append(1)
            lst.append(lst_i)
        return lst
                
            
