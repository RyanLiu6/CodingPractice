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
