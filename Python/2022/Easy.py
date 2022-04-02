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

        # Here, k is the both the count and index
        k = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()

examples_27 = {
    3: [3,2,2,3],
    2: [0,1,2,2,3,0,4,2],
    4: [2],
    1: [1]
}

for key, val in examples_27.items():
    print("=================================")
    k = solution.remove_element(val, key)
    print(k, val[:k])


# list1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
# list2 = ListNode(1, next=ListNode(3, next=ListNode(4)))

# result = solution.merge_two_lists(list1, list2)

# while result.next:
#     print(result.val)
#     result = result.next
