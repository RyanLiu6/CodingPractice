from Introduction import *

intSoln = IntroSoln()
# test = TreeNode(10)
# test.left = TreeNode(5)
# test.right = TreeNode(15)
# test.right.left = TreeNode(6)
# test.right.right = TreeNode(20)

test = TreeNode(0)
test.right = TreeNode(-1)

print(intSoln.isValidBST(test))
