from Conclusion import *
from TraverseTree import *


def main():
    traSoln = TraverseSolutions()
    conSoln = ConcluSolutions()

    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test.left.right = TreeNode(4)

    # test = TreeNode(3)
    # test.left = TreeNode(5)
    # test.right = TreeNode(1)
    # test.left.left = TreeNode(6)
    # test.left.right = TreeNode(2)
    # test.left.right.left = TreeNode(7)
    # test.left.right.right = TreeNode(4)
    # test.right.left = TreeNode(0)
    # test.right.right = TreeNode(8)

    # res = conSoln.deserialize(conSoln.serialize(test))
    #
    # print(traSoln.levelOrder(res))
    # print(traSoln.levelOrder(test))

    print(conSoln.lowestCommonAncestor(test, test.left.right, test.right).val)

if __name__ == "__main__":
    main()
