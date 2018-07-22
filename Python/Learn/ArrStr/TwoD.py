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
        row = len(matrix)
        col = len(matrix[0])
        retList = []

        for i in range(col):
            for j in range(row):
                retList.append(matrix[j][i])

        print(retList)

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])
        retList = []

        visited = [[False for _ in range(col)] for __ in range(row)]

        row -= 1
        col -= 1

        def spiralHelper(i, j, direction):
            if direction == "right" and j <= col and not visited[i][j]:
                retList.append(matrix[i][j])
                visited[i][j] = True
                print(direction)
                print(i, j)
                spiralHelper(i, j + 1, "right")
            else:
                spiralHelper(i + 1, j, "down")

            if direction == "down" and i <= row and not visited[i][j]:
                retList.append(matrix[i][j])
                print(direction)
                print(i, j)
                visited[i][j] = True
                spiralHelper(i + 1, j, "down")
            else:
                spiralHelper(i, j - 1, "left")

            if direction == "left" and j >= -1 and not visited[i][j]:
                retList.append(matrix[i][j])
                print(direction)
                print(i, j)
                visited[i][j] = True
                spiralHelper(i, j - 1, "left")
            else:
                spiralHelper(i - 1, j, "up")

            if direction == "up" and i >= -1 and not visited[i][j]:
                retList.append(matrix[i][j])
                visited[i][j] = True
                print(direction)
                print(i, j)
                spiralHelper(i - 1, j, "up")
            else:
                spiralHelper(i, j + 1, "right")

        spiralHelper(0, 0, "right")
        print(visited)
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
