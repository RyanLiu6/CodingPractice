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

