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
