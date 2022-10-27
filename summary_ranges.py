from typing import List


class Solution:
    def summary_ranges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            begin = nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i = i + 1
            end = nums[i]
            if begin == end:
                result.append(str(begin))
            else:
                result.append(str(begin) + "->" + str(end))
            i = i + 1
        return result


if __name__ == "__main__":
    nums = [0, 2, 3, 4, 6, 8, 9]
    sol = Solution()
    print(sol.summary_ranges(nums))

