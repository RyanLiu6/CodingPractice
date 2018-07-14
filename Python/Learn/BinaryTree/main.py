from Conclusion import *
from TraverseTree import *


def main():
    traSoln = TraverseSolutions()
    conSoln = ConcluSolutions()

    # test = TreeNode(1)
    # test.left = TreeNode(2)
    # test.right = TreeNode(3)
    # test.right.left = TreeNode(4)
    # test.right.right = TreeNode(5)
    #
    # res = conSoln.deserialize(conSoln.serialize(test))
    #
    # print(traSoln.levelOrder(res))
    # print(traSoln.levelOrder(test))

    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]

    conSoln.buildTree(inorder, postorder)

    conSoln.buildTree([], [])


if __name__ == "__main__":
    main()
