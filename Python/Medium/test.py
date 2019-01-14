from ArrStrSolutions import *
from TreeGraphSolutions import *
from BackTrackSolutions import *
from MathSolutions import *
from SortSearchSolutions import *
from OtherSolutions import *
from DPSolutions import *
from MiscSolutions import *
import collections


# arrSoln = ArrStrSolutions()
# print(arrSoln.threeSum([-1, 0, 1, 2, -1, -4]))
# print(arrSoln.lengthOfLongestSubstring("abcabcbb"))
# print(arrSoln.lengthOfLongestSubstring("bbbbb"))
# print(arrSoln.lengthOfLongestSubstring("pwwkew"))
# print(arrSoln.longestPalindrome("babad"))
# print(arrSoln.longestPalindrome("a"))

# test = TreeNode(1)
# test.left = TreeNode(2)
# test.right = TreeNode(3)
# test.left.left = TreeNode(4)
# test.right.right = TreeNode(5)
#
# treeSoln = TreeGraphSolutions()
# print(treeSoln.zigzagLevelOrder(test))

# arr = [2,0,2,1,1,0]
# sSoln = SortSearchSolutions()
# sSoln.sortColors(arr)
# print(arr)
# print(sSoln.searchRange([5,7,7,8,8,10], 8))
# print(sSoln.searchRange([1], 1))
# print(sSoln.search([4,5,6,7,0,1,2], 0))

# matrix = [
#   [1,   4,  7],
#   [2,   5,  8],
#   [3,   6,  9]
# ]
#
# print(sSoln.searchMatrix(matrix, 5))

# bSolns = BackSolutions()
# print(bSolns.letterCombinations("23"))
# print(bSolns.subsets(["g", "a", "f", "t"]))

# mSoln = MathSolutions()
# print(mSoln.myPow(2.100, 3))
# print(mSoln.myPow(2.000, -2))
# print(mSoln.mySqrt(121))
# print(mSoln.titleToNumber("ABC"))
# print(mSoln.divide(10, 3))
# print(mSoln.divide(7, -3))
# print(mSoln.divide(-1, 1))

# oSoln = OtherSolutions()
# print(oSoln.evalRPN(["4", "13", "5", "/", "+"]))
# print(oSoln.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(oSoln.majorityElement([2,2,1,1,1,2,2]))

# dpSoln = DPSolutions()
# print(dpSoln.canJump([2,3,1,1,4]))
# print(dpSoln.canJump([3,2,1,0,4]))
# print(dpSoln.uniquePaths(3, 2))
# print(dpSoln.uniquePaths(7, 3)
# print(dpSoln.coinChange([1,2,5], 11))
# print(dpSoln.coinChange([186,419,83,408], 6249))
# print(dpSoln.lengthOfLIS([10,9,2,5,3,7,101,18]))

miscSoln = MiscSolutions()
testTree = TreeNode(10)
testTree.left = TreeNode(5)
testTree.right = TreeNode(15)
testTree.left.left = TreeNode(3)
testTree.left.right = TreeNode(7)
testTree.right.right = TreeNode(18)
# print(miscSoln.rangeSumBST(testTree, 7, 15))
