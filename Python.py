# -----------------------------------------------------------
# Two Sum Problem (LeetCode-style)
#
# This script defines a `Solution` class that implements a
# hash-map-based solution to the classic Two Sum problem.
# Given an array and a target, it finds two indices such that
# the numbers at those indices sum to the target.
# -----------------------------------------------------------

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found 
# -----------------------------------------------------------
# Conclusion:
# This efficient solution leverages a hash map to achieve
# O(n) time complexity, making it suitable for large arrays.
# -----------------------------------------------------------