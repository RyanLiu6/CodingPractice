from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for key, val in enumerate(nums):
            nums_dict[val] = key

        for key, val in enumerate(nums):
            to_find = target - val
            if to_find in nums_dict and nums_dict[to_find] != key:
                return [key, nums_dict[to_find]]
