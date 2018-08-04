from HashSet import *
from HashMap import *
from Key import *
from Conclusion import *

setSoln = HashSetSolution()
# print(setSoln.containsDuplicate([1,2,3,1]))
# print(setSoln.intersection([1,2,2,1], [2,2]))
# print(setSoln.isHappy(19))

mapSoln = HashMapSolution()
# print(mapSoln.isIsomorphic("egg", "add"))
# print(mapSoln.isIsomorphic("foo", "bar"))
# print(mapSoln.isIsomorphic("paper", "title"))
# print(mapSoln.isIsomorphic("ab", "aa"))
# print(mapSoln.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))
# print(mapSoln.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
# print(mapSoln.intersect([1,2,2,1], [2,2]))
# print(mapSoln.containsNearbyDuplicate([1,2,3,1], 3))
# print(mapSoln.containsNearbyDuplicate([1,0,1,1], 1))
# print(mapSoln.containsNearbyDuplicate([1,2,3,1,2,3], 2))

Input = [
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

testTree = TreeNode(1)
testTree.left = TreeNode(2)
testTree.right = TreeNode(3)
testTree.left.left = TreeNode(4)
testTree.right.left = TreeNode(2)
testTree.right.right = TreeNode(4)
testTree.right.left.left = TreeNode(4)

keySoln = KeySolution()
# print(keySoln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(keySoln.isValidSudoku(Input))
# print(keySoln.findDuplicateSubtrees(testTree))

conSoln = ConcluSolution()
# print(conSoln.topKFrequent([1,1,1,2,2,3], 2))
# print(conSoln.topKFrequent([2,3,4,1,4,0,4,-1,-2,-1], 2))
print(conSoln.lengthOfLongestSubstring("abcabcbb"))
