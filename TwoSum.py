class Solution():
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            print("Iteration:", i)
            j_starting_point = i + 1
            for j, number in enumerate(nums[j_starting_point:]):
                print("Jiteration:", j + j_starting_point)
                if num + number == target:
                    return [i, j + j_starting_point]
                
mySolution = Solution()

print(mySolution.twoSum([2,3,5], 8))