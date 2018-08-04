class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class KeySolution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        retList = []
        if not strs:
            return retList

        anaMap = {}
        index = 0

        for str in strs:
            curr = "".join(sorted(str))
            if curr in anaMap:
                retList[anaMap[curr]].append(str)
            else:
                anaMap[curr] = index
                retList.append([str])
                index += 1

        return retList

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        Input:
        [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
        Output: true
        """
        return self.isRowValid(board) and self.isColValid(board) and self.isSquareValid(board)

    def isRowValid(self, board):
        rowDict = {}
        for row in board:
            for c in row:
                if c != "." and c in rowDict:
                    return False
                else:
                    rowDict[c] = 1
            rowDict.clear()
        return True

    def isColValid(self, board):
        colDict = {}
        for i in range(len(board[0])):
            for row in board:
                if row[i] != "." and row[i] in colDict:
                    return False
                else:
                    colDict[row[i]] = 1
            colDict.clear()
        return True

    def isSquareValid(self, board):
        squareDict = {}
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                for c in square:
                    if c != "." and c in squareDict:
                        return False
                    else:
                        squareDict[c] = 1
                squareDict.clear()
        return True

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        treeDict = {}
        result = []

        def dupSubtreeHelper(node):
            if not node:
                return "#"

            currStr = ""
            currStr += str(node.val) + "|"
            currStr += dupSubtreeHelper(node.left) + "|"
            currStr += dupSubtreeHelper(node.right)

            val = treeDict.get(currStr, 0)
            if val == 1:
                result.append(node)
            treeDict[currStr] = val + 1

            return currStr

        dupSubtreeHelper(root)
        return result
