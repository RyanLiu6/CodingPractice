from ArrStrSolutions import *
from LLSolutions import *
from BackSolutions import *
from topologicalSort import *
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

aSoln = ArrStrSolutions()
# print(aSoln.validPalindromeII("abcdca"))
# print(aSoln.maxSubArrayLen([1, -1, 5, -2, 3], 3))
# print(aSoln.maxSubArrayLen([-2, -1, 2, 1], 1))
# print(aSoln.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# test = TreeNode(1)
# test.left = TreeNode(2)
# test.right = TreeNode(5)
# lSoln = LLSolutions()
# lSoln.flatten(test)
#
# bSoln = BackSolutions()
# print(bSoln.permuteUnique([1,1,2]))

# tsSoln = tsSolution()
# print(tsSoln.canFinish(2, [[1,0]]))
# tsSoln.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])

h = []
heapq.heappush(h, (1, ListNode(1)))
heapq.heappush(h, (1, ListNode(1)))
heapq.heappush(h, (2, ListNode(2)))
print(heapq.heappop(h))
