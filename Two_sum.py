from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for index, value in enumerate(nums):
            difference = target- value
            if difference in values:
                return [values[difference], index]
            else: values[value] = index

