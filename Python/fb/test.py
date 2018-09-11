from ArrStrSolutions import *
from LLSolutions import *
from BackSolutions import *


aSoln = ArrStrSolutions()
# print(aSoln.validPalindromeII("abcdca"))
# print(aSoln.maxSubArrayLen([1, -1, 5, -2, 3], 3))
# print(aSoln.maxSubArrayLen([-2, -1, 2, 1], 1))
# print(aSoln.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

test = TreeNode(1)
test.left = TreeNode(2)
test.right = TreeNode(5)
lSoln = LLSolutions()
lSoln.flatten(test)

bSoln = BackSolutions()
print(bSoln.permuteUnique([1,1,2]))
