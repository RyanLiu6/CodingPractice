from ArraySolutions import *
from StringSolutions import *
from SortSearchSolutions import *
from MathSolutions import *
from OtherSolutions import *
from DynamicSolutions import *


def main():
    arrSoln = ArraySolutions()
    # print(arrSoln.removeDuplicates([1,1,2]))
    # print(arrSoln.maxProfit([7,1,5,3,6,4]))
    # print(arrSoln.rotate([1,2,3,4,5,6,7],3))
    # print(arrSoln.rotate([1,2,3,4,5,6],2))
    # print(arrSoln.plusOne([1,2,3]))
    # print(arrSoln.moveZeroes([0,1,0,3,12]))

    strSoln = StringSolutions()
    # print(strSoln.isAnagram("rat", "art"))
    # print(strSoln.reverse(123))
    # print(strSoln.reverse(1534236469))
    # print(strSoln.isPalindrome("0P"))
    # print(strSoln.strStr("a","a"))
    # print(strSoln.myAtoi("+0 123"))
    # print(strSoln.countAndSay(3))
    # print(strSoln.longestCommonPrefix(["flower","flow","flight"]))

    sortSoln = SortSearchSolutions()
    # sortSoln.merge([1,2,4,5,6,0], 5, [3], 1)
    # sortSoln.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
    # print(sortSoln.firstBadVersion(5))

    mathSoln = MathSolutions()
    # print(mathSoln.countPrimes(10))
    # print(mathSoln.isPowerOfThree(27))
    # print(mathSoln.romanToInt("IV"))

    othSoln = OtherSolutions()
    # print(othSoln.hammingWeight(11))
    # print(othSoln.hammingWeight(128))
    # print(othSoln.reverseBits(43261596))
    print(othSoln.isValid("()"))
    # print(othSoln.isValid("([)]"))

    dpSoln = DPSolutions()
    # print(dpSoln.climbStairs(2))
    # print(dpSoln.climbStairs(3))
    # print(dpSoln.maxProfit([7,1,5,3,6,4]))
    # print(dpSoln.maxProfit([2,4,1]))
    # print(dpSoln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    # print(dpSoln.maxSubArray([-2,1]))
    # print(dpSoln.rob([1,2,3,1]))
    # print(dpSoln.rob([2,7,9,3,1]))

if __name__ == "__main__":
    main()
