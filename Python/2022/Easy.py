from calendar import c
from re import I
import sys

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Leetcode Problem #21

        LinkedList problems often needs a root node and a current node to iterate.

        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        """

        # Iterative
        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        elif not list1 and not list2:
            return None

        merge_root: ListNode = None
        if list1.val < list2.val:
            merge_root = list1
            list1 = list1.next
        else:
            merge_root = list2
            list2 = list2.next

        # Iterate until one is empty
        current: ListNode = merge_root
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Check if there's anything leftover
        if list1:
            current.next = list1
        else:
            current.next = list2

        return merge_root

        # Recursive
        """
        Build base case - if either is None, we return the other

        Small case:
        list1 = [1]
        list2 = [2]
        output = [1, 2]

        More complex case:
        list1 = [1, 3]
        list2 = [2, 4]
        output = [1, 2, 3, 4]
        """
        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        elif not list1 and not list2:
            return None

        if list1.val < list2.val:
            list1.next = self.merge_two_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists(list1, list2.next)
            return list2

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Leetcode Problem #26

        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same.

        Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]

        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

        Steps:
        1. Encounter unique -> index i
        2. Find next unique -> index j
        3. Swap index i + 1 with j
        4. Repeat
        """
        if not nums:
            return 0

        # Here, k is both the count and index
        k = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i]
                k += 1

        # At this point, we know that nums[n - 2] != nums[n - 1], and therefore nums[n - 1] is another unique
        nums[k] = nums[n - 1]

        return k + 1

    def remove_element(self, nums: List[int], val: int) -> int:
        """
        Leetcode Problem #27

        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The relative order of the elements may be changed.

        Return k after placing the final result in the first k slots of nums.

        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]

        Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums = [0,1,4,0,3,_,_,_]
        Note that the first five elements can be returned in any order.
        """
        if not nums:
            return 0

        # Here, k is both the count and index
        k = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


    def str_str(self, haystack: str, needle: str) -> int:
        """
        Leetcode Problem #28

        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Input: haystack = "hello", needle = "ll"
        Output: 2

        Input: haystack = "aaaaa", needle = "bba"
        Output: -1
        """
        # Simplistic solution that isn't accepted
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

        # Actual solution
        if not needle:
            return -1

        n = len(needle)
        m = len(haystack)
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1

    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Leetcode Problem #35

        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        Input: nums = [1,3,5,6], target = 2
        Output: 1

        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Input: nums = [1,3,5,6], target = 7
        Output: 4
        """
        # No constraints on runtime
        if not nums:
            return 0

        for key, val in enumerate(nums):
            if val >= target:
                return key

        # If it wasn't found AND we haven't returned yet, must be last element
        return len(nums)

        # Following constraint of runtime complexity using Binary Search
        if not nums:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end + start) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif mid_value < target:
                start = mid + 1
            else:
                end = mid - 1

        return start

    def max_sub_array(self, nums: List[int]) -> int:
        """
        Leetcode Problem #53

        Given an integer array nums, find the contiguous subarray (containing at least one number)
        which has the largest sum and return its sum.

        A subarray is a contiguous part of an array.

        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6

        Input: nums = [1]
        Output: 1

        Input: nums = [5,4,-1,7,8]
        Output: 23

        Iterate over nums, since nums can contain negative numbers, we need to be careful!

        Given that we're looking for contiguous subarrays, we should be comparing the current
        num vs the sum so far. If num > curr_sum, then curr_sum = num.
        """
        curr_sum = nums[0]
        max_sum = curr_sum

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def length_of_last_word(self, s: str) -> int:
        """
        Leetcode Problem #58

        Given a string s consisting of some words separated by some number of spaces,
        return the length of the last word in the string.

        A word is a maximal substring consisting of non-space characters only.
        """
        words = s.strip().split()
        return len(words[-1])

    def plus_one(self, digits: List[int]) -> List[int]:
        """
        Leetcode Problem #66

        You are given a large integer represented as an integer array digits,
        where each digits[i] is the ith digit of the integer.

        The digits are ordered from most significant to least significant in left-to-right order.
        The large integer does not contain any leading 0's.

        Increment the large integer by one and return the resulting array of digits.

        Input: digits = [1,2,3]
        Output: [1,2,4]

        Input: digits = [4,3,2,1]
        Output: [4,3,2,2]

        Input: digits = [9]
        Output: [1,0]
        """
        if not digits:
            return digits

        nums = []
        carry = False
        n = len(digits)

        for i in range(n):
            val = digits[n - i - 1]

            if i == 0:
                carry = True

            if carry:
                val += 1
                if val > 9:
                    val %= 10
                    carry = True
                else:
                    carry = False

            nums.append(val)

        if carry:
            nums.append(1)

        return nums[::-1]

        # Better solution
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            curr = digits[i] + carry
            carry = curr // 10

            digits[i] = curr % 10

        if carry:
            digits.insert(0, 1)

        return digits

    def add_binary(self, a: str, b: str) -> str:
        """
        Leetcode Problem #67:

        Given two binary strings a and b, return their sum as a binary string.

        Input: a = "11", b = "1"
        Output: "100"

        Input: a = "1010", b = "1011"
        Output: "10101"
        """
        n = len(a) - 1
        m = len(b) - 1
        carry = 0
        result = []

        # End loop once we are done with one string
        while n >= 0 and m >= 0:
            curr = int(a[n]) + int(b[m]) + carry
            carry = curr // 2

            result.insert(0, str(curr % 2))

            n -= 1
            m -= 1

        # Repeat above logic for what's left of n and m
        for i in range(n, -1, -1):
            curr = int(a[i]) + carry
            carry = curr // 2

            result.insert(0, str(curr % 2))

        for j in range(m, -1, -1):
            curr = int(b[j]) + carry
            carry = curr // 2

            result.insert(0, str(curr % 2))

        # Check carry one last time
        if carry:
            result.insert(0, str(1))

        return "".join(result)


    def my_sqrt(self, x: int) -> int:
        """
        Leetcode Problem #69:

        Given a non-negative integer x, compute and return the square root of x.

        Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

        Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

        Input: x = 4
        Output: 2

        Input: x = 8
        Output: 2
        Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
        """

        """
        Naive divide by 2 solution:
        A few base cases:
        x = 0 -> return 0
        x = 1 -> return 1

        1. sqrt(4) = 2^2 -> 4 // 2 = 2 so we have to go up to 2
        2. sqrt(8) ~= 2.8 -> 8 // 2 = 4, we would hit 3 * 3 = 9 and 9 > 8 so return 3 - 1 = 2
        3. sqrt(9) = 3^2 -> 9 // 2 = 4 -> going up to 4 is good enough
        """
        # if x == 0 or x == 1:
        #     return x

        # for num in range(1, (x // 2) + 1):
        #     squared = num * num

        #     if squared == x:
        #         return num
        #     elif squared >= x:
        #         return num - 1

        # # In the case that we couldn't hit, return num
        # return num

        """
        Binary Search Answer
        """
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared > x:
                right = mid - 1
            else:
                left = mid + 1

        # Because parameter x doesn't have to be a perfect square, this means that we won't find the answer sometimes
        # Thus we have to look for highest number num such that num * num <= x. If it's num * num > x, we found the closest!
        return mid if mid * mid < x else mid - 1

solution = Solution()

# examples_26 = [
#     [1,1,2],
#     [0,0,0,1,1],
#     [0,0,1,1,1,2,2,3,3,4]
# ]

# for item in examples_26:
#     print("=================================")
#     k = solution.remove_duplicates(item)
#     print("Solution: ")
#     print(k, item[:k])


# examples_27 = {
#     3: [3,2,2,3],
#     2: [0,1,2,2,3,0,4,2],
#     4: [2],
#     1: [1]
# }

# for key, val in examples_27.items():
#     print("=================================")
#     k = solution.remove_element(val, key)
#     print(k, val[:k])

# examples_28 = {
#     "hello": "ll",
#     "aaaaa": "bba",
#     "a": "a",
# }

# for key, val in examples_28.items():
#     print("=================================")
#     print(solution.str_str(key, val))

# examples_35 = {
#     2: [1,3,5,6],
#     5: [1,3,5,6],
#     7: [1,3,5,6],
#     4: [1,3,5]
# }

# for key, val in examples_35.items():
#     print("=================================")
#     print(solution.search_insert(val, key))

# examples_53 = [
#     [-2,1,-3,4,-1,2,1,-5,4],
#     [1],
#     [5,4,-1,7,8]
# ]

# for item in examples_53:
#     print(solution.max_sub_array(nums=item))

# examples_66 = [
#     [1,2,3],
#     [4,3,2,1],
#     [9]
# ]

# for item in examples_66:
#     print("=================================")
#     print(solution.plus_one(item))

examples_67 = [
    ["11", "1"],
    ["1010", "1011"]
]

for item in examples_67:
    print("=================================")
    print(solution.add_binary(item[0], item[1]))

# examples_69 = [0, 1, 2, 3, 4, 8, 9]

# for item in examples_69:
#     print("=================================")
#     print(solution.my_sqrt(item))

# list1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
# list2 = ListNode(1, next=ListNode(3, next=ListNode(4)))

# result = solution.merge_two_lists(list1, list2)

# while result.next:
#     print(result.val)
#     result = result.next
