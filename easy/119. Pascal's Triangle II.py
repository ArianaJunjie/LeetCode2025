class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        lst = [[1], [1,1]]
        for i in range(2, rowIndex+1):
            lst_i = []
            lst_i.append(1)
            for j in range(len(lst[i-1])-1):
                lst_i.append(lst[i-1][j] + lst[i-1][j+1])
            lst_i.append(1)
            lst.append(lst_i)
        return lst[rowIndex]
                
            

        