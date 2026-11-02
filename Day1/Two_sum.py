class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, x in enumerate(nums):
            needed = target - x

            if needed in seen:
                return [seen[needed], i]

            seen[x] = i

        return []


if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
