from fib import *
from ArraySolutions import *
from StringSolutions import *


def main():
    print("We are at Main\n")
    arrSoln = ArraySolutions()
    # print(arrSoln.removeDuplicates([1,1,2]))
    # print(arrSoln.maxProfit([7,1,5,3,6,4]))
    # print(arrSoln.rotate([1,2,3,4,5,6,7],3))
    # print(arrSoln.rotate([1,2,3,4,5,6],2))
    # print(arrSoln.plusOne([1,2,3]))
    # print(arrSoln.moveZeroes([0,1,0,3,12]))

    strSoln = StringSolutions()
    print(strSoln.isAnagram("rat", "art"))

    # fib = Fib(10)
    # print(fib.getFib(25))

if __name__ == "__main__":
    main()
