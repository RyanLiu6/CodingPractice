class TwoDSolution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        Input:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        Output:  [1,2,4,7,5,3,6,8,9]
        """
        retList = []
        if not matrix:
            return retLst

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        retList = []
        if not matrix:
            return retList

        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1

        while rowStart <= rowEnd and colStart <= colEnd:
            # Go right
            for i in range(colStart, colEnd + 1):
                retList.append(matrix[rowStart][i])
            rowStart += 1

            # Go down
            for i in range(rowStart, rowEnd + 1):
                retList.append(matrix[i][colEnd])
            colEnd -= 1

            # Go left
            if rowStart <= rowEnd:
                for i in range(colEnd, colStart - 1, -1):
                    retList.append(matrix[rowEnd][i])
            rowEnd -= 1

            # Go Up
            if colStart <= colEnd:
                for i in range(rowEnd, rowStart - 1, -1):
                    retList.append(matrix[i][colStart])
            colStart += 1

        return retList

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        Input: 5
        Output:
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]
        """
        resList = []

        for i in range(numRows):
            if i == 0:
                rowList = [1]
            elif i == 1:
                rowList = [1,1]
            else:
                rowList = []
                for j in range(i + 1):
                    if j == 0:
                        rowList.append(1)
                    elif j == i:
                        rowList.append(1)
                    else:
                        curr = resList[i - 1][j - 1] + resList[i - 1][j]
                        rowList.append(curr)
            resList.append(rowList)
        return resList
