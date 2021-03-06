"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = n + nums[l] + nums[r]
                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:  # sum3 == 0
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


class TestSolution(unittest.TestCase):
    def test_threeSum(self):
        solution = Solution()
        nums = [-1, 0, 1, 2, -1, -4]
        expected = sorted([[-1, -1, 2], [-1, 0, 1]])
        output = sorted(solution.threeSum(nums))
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
