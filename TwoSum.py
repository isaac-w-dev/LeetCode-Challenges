# CHALLENGE VERSION: ALGORITHM LESS THAN 0(n^2) TIME COMPLEXITY
class Solution():
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            j_starting_point = i + 1
            for j, number in enumerate(nums[j_starting_point:]):
                if num + number == target:
                    return [i, j + j_starting_point]