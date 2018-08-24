from ArrStrSolutions import *
from TreeGraphSolutions import *
from BackTrackSolutions import *
from MathSolutions import *
from SortSearchSolutions import *


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

arr = [2,0,2,1,1,0]
sSoln = SortSearchSolutions()
sSoln.sortColors(arr)
print(arr)

# bSolns = BackSolutions()
# print(bSolns.letterCombinations("23"))
# print(bSolns.subsets([1,2,3]))

# mSoln = MathSolutions()
# print(mSoln.myPow(2.100, 3))
# print(mSoln.myPow(2.000, -2))
# print(mSoln.mySqrt(121))
# print(mSoln.titleToNumber("ABC"))
# print(mSoln.divide(10, 3))
# print(mSoln.divide(7, -3))
# print(mSoln.divide(-1, 1))
