class Solution(object):
    def twoSum(self, nums, target):
        # Lưu các số đã gặp theo dạng giá trị -> chỉ số
        seen = {}

        # Duyệt từng phần tử cùng chỉ số của nó
        for i, x in enumerate(nums):
            # Tính số cần ghép với x để có tổng bằng target
            needed = target - x

            # Nếu số cần tìm đã xuất hiện, trả về hai chỉ số
            if needed in seen:
                return [seen[needed], i]

            # Lưu phần tử hiện tại để dùng ở các bước sau
            seen[x] = i

        return []

if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))