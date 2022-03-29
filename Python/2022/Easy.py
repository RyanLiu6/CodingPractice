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

    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Leetcode Problem #14

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
        """
        if not strs:
            return ""

        """
        We take our potential prefix, our seed, as the shortest string in the list.
        This can be achieved via sorting first, or via the min function.
        """
        seed = min(strs, key=len)

        for index, letter in enumerate(seed):
            for word in strs:
                if word[index] != letter:
                    return seed[:index]

        return seed

    def is_valid(self, s: str) -> bool:
        """
        Leetcode Problem #20

        Input: s = "()"
        Output: true

        Input: s = "(]"
        Output: false
        """
        if not s:
            return False

        opening = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        closing = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for item in s:
            if item in opening:
                stack.append(item)
            else:
                # If it isn't opening, must be closing since string s can only contain opening or closing
                try:
                    matching = stack.pop()
                except IndexError:
                    return False
                else:
                    if closing[item] != matching:
                        return False

        if len(stack) != 0:
            return False
        else:
            return True

solution = Solution()
print(solution.is_valid("()"))
