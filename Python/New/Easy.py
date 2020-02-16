from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret_list = []

        if not nums:
            return ret_list

        complement = {}

        for key, val in enumerate(nums):
            complement[val] = key

        for key, val in enumerate(nums):
            want = target - val
            if want in complement and key != complement[want]:
                return [key, complement[want]]

        return []

    def reverse(self, x: int) -> int:
        is_neg = True if x < 0 else False
        x = abs(x)

        ret_num = 0
        min_int = -1 << 31
        max_int = (1 << 31) - 1

        while x > 0:
            ret_num = ret_num * 10 + x % 10
            x = x // 10

            if ret_num > max_int or ret_num < min_int:
                return 0

        if is_neg:
            ret_num *= -1

        return ret_num

    def isPalindrome(self, x: int) -> bool:
        """
        If x is negative, then it cannot be a Palindrome
        If x is divisible by 10, then the first digit must be 0 but that cannot be
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        forward = x
        backward = 0

        while x > 0:
            backward = backward * 10 + x % 10
            x = x // 10

        return forward == backward

    def romanToInt(self, s: str) -> int:
        roman_value = 0

        if not s:
            return roman_value

        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        """
        Subtraction rules:
        1. I before V and X for 4 and 9
        2. X before L and C for 40 and 90
        3. C before D and M for 400 and 900

        Note: Roman numerals are always DESCENDING unless subtraction

        Hence:
        1. IV is (1 + 5) - 2(1) = 4
        2. IX is (1 + 10) - 2(1) = 9
        3. XL is (10 + 50) - 2(10) = 40 ...
        """

        prev = 1 << 31
        for x in s:
            curr = values[x]
            if curr > prev:
                roman_value += curr - 2 * prev
            else:
                roman_value += curr

            prev = curr

        return roman_value

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Get shortest string in list
        seed = min(strs, key=len)

        # Check and compare each character
        for index in range(len(seed)):
            for s in strs:
                if s[index] != seed[index]:
                    return seed[:index]

        return seed

    # def isValid(self, s: str) -> bool:
    #     return False

soln = Solution()
# print(soln.isValid("()"))
# print(soln.isValid("()[]{}"))
# print(soln.isValid("(]"))
# print(soln.isValid("([)]"))
# print(soln.isValid("{[]}"))
