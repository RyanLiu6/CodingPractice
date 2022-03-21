from Introduction import *
from TwoD import *
from TwoPointer import *
from Conclusion import *

test = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

test1 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

intSoln = IntroSolution()
# print(intSoln.pivotIndex([1, 7, 3, 6, 5, 6]))
# print(intSoln.addBinary("111", "11"))

twoSoln = TwoDSolution()
# twoSoln.findDiagonalOrder([[1, 2, 3, 4], [5, 6, 7, 8]])
# twoSoln.findDiagonalOrder(test)

# print(twoSoln.spiralOrder(test))
# print(twoSoln.spiralOrder(test1))

# twoSoln.generate(5)

twoPSoln = TwoPSolution()
# twoPSoln.arrayPairSum([1,2,3,4])
# print(twoPSoln.findMaxConsecutiveOnes([1,1,0,1,1,1,1]))
# print(twoPSoln.minSubArrayLen(7, [2,3,1,2,4,3]))
# print(twoPSoln.minSubArrayLen(15, [1,2,3,4,5]))

conSoln = ConcluSolution()
print(conSoln.getRow(3))
# print(conSoln.reverseWords_II("the sky is blue"))
# print(conSoln.reverseWords_III("Let's take LeetCode contest"))
