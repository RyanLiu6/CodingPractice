from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Leetcode Problem #1
        """
        nums_dict = {}

        for key, val in enumerate(nums):
            nums_dict[val] = key

        for key, val in enumerate(nums):
            to_find = target - val
            if to_find in nums_dict and nums_dict[to_find] != key:
                return [key, nums_dict[to_find]]

    def is_palindrome(self, x: int) -> bool:
        """
        Leetcode Problem #2
        """

        # Simple Python String hack
        string_int = str(x)
        return string_int == string_int[::-1]

        # Actual palindrome solution
        """
        Easy cases to rule out:
        If x is negative, then it cannot be a Palindrome
        If x is divisible by 10, then the first digit must be 0 but that cannot be

        https://www.code-recipe.com/post/palindrome-number
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        forward = x
        backward = 0

        while x > 0:
            backward = backward * 10 + x % 10
            x = x // 10

        return forward == backward

    def roman_to_int(self, s: str) -> int:
        """
        Leetcode Problem #13

        Subtraction rules:
        1. I before V and X for 4 and 9
        2. X before L and C for 40 and 90
        3. C before D and M for 400 and 900

        Note: Roman numerals are always DESCENDING unless subtraction

        Input: s = "MCMXCIV"
        Output: 1994

        M = 1000
        CM = 900
        XC = 90
        IV = 4
        """
        roman_value = 0

        if not s:
            return roman_value

        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        previous = 0
        for item in s:
            current = roman_dict[item]
            if current > previous:
                roman_value += current - 2*previous
            else:
                roman_value += current

            previous = current

        return roman_value
