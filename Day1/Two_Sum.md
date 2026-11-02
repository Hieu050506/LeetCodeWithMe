# Day 1: Two Sum — Tổng hai số

**Độ khó:** Dễ (Easy)

## Đề bài

Cho mảng số nguyên `nums` và số nguyên `target`. Trả về chỉ số của hai phần tử có tổng bằng `target`.

- Mỗi đầu vào có đúng một lời giải.
- Không được sử dụng cùng một phần tử hai lần.
- Có thể trả về hai chỉ số theo bất kỳ thứ tự nào.
- Chỉ số của mảng bắt đầu từ `0`.

### Ví dụ 1

```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

Giải thích: `nums[0] + nums[1] = 2 + 7 = 9`.

### Ví dụ 2

```text
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

Giải thích: `nums[1] + nums[2] = 2 + 4 = 6`.

### Ví dụ 3

```text
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

Giải thích: Hai phần tử có cùng giá trị `3` nhưng ở hai chỉ số khác nhau.

### Ràng buộc

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Chỉ có đúng một đáp án hợp lệ.

**Yêu cầu mở rộng:** Tìm thuật toán có độ phức tạp thời gian tốt hơn `O(n²)`.

## Thuật toán giải quyết

**Đầu vào:**

- Mảng số nguyên `nums`.
- Số nguyên `target` là tổng cần tìm.

**Đầu ra:**

- Hai chỉ số khác nhau `[i, j]` sao cho `nums[i] + nums[j] == target`.

### Các bước thực hiện:

1. Tạo dictionary rỗng `seen` để lưu các số đã gặp theo dạng `giá trị: chỉ số`.
2. Duyệt từng phần tử, với `i` là chỉ số và `x` là giá trị hiện tại.
3. Tính số cần ghép với `x`: `needed = target - x`.
4. Kiểm tra `needed` trong dictionary:
   - Nếu đã có, trả về `[seen[needed], i]`.
   - Nếu chưa có, lưu `seen[x] = i` rồi tiếp tục duyệt.
5. Trả về `[]` nếu không tìm thấy. Theo giả thiết của đề, trường hợp này không xảy ra.

## Code Python

Đoạn code dưới đây dùng đúng mẫu `class Solution(object)` và `def twoSum(self, nums, target):`, đồng nhất với phần lời giải trong [Two_sum.py](Two_sum.py). Khi nộp trên LeetCode, chép phần lớp và hàm này:

```python
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
```

## Giải thích code

### 1. Khai báo lớp và hàm

```python
class Solution(object):
    def twoSum(self, nums, target):
```

`Solution` là lớp chứa lời giải. Hàm `twoSum` dùng đúng các tham số trong mẫu đề bài:

- `self`: Đại diện cho đối tượng đang gọi hàm. Python tự truyền giá trị này.
- `nums`: Danh sách số nguyên cần tìm cặp.
- `target`: Tổng mà hai số phải đạt được.

Ví dụ gọi hàm: `Solution().twoSum([2, 7, 11, 15], 9)`. Bạn chỉ truyền `nums` và `target`; Python tự xử lý `self`.

Ba dòng `:type nums: List[int]`, `:type target: int` và `:rtype: List[int]` trong docstring mô tả kiểu đầu vào và đầu ra. Chúng cho biết hàm nhận một danh sách số nguyên, một số nguyên và trả về danh sách chỉ số.

### 2. Tạo nơi lưu các số đã gặp

`seen = {}` tạo một dictionary rỗng, lưu theo dạng `giá trị: chỉ số`. Ví dụ `{2: 0}` nghĩa là đã gặp số `2` tại chỉ số `0`.

### 3. Duyệt từng phần tử

`for i, x in enumerate(nums):` lấy đồng thời chỉ số `i` và giá trị `x`. Với `[2, 7, 11, 15]`, lượt đầu có `i = 0`, `x = 2`.

### 4. Tính số còn thiếu

`needed = target - x` tính số cần ghép với `x`. Nếu `target = 9` và `x = 7` thì `needed = 2`.

### 5. Kiểm tra và trả về đáp án

`if needed in seen:` kiểm tra số cần tìm đã xuất hiện trước đó hay chưa. Nếu đã có, `return [seen[needed], i]` trả về chỉ số đã lưu cùng chỉ số hiện tại.

Ví dụ đang xét số `7` ở chỉ số `1`, dictionary đã có `{2: 0}`. Vì `2 + 7 = 9`, hàm trả về `[0, 1]`.

### 6. Lưu phần tử hiện tại

Nếu chưa tìm được cặp, `seen[x] = i` ghi nhớ phần tử hiện tại cho các lượt sau. Phải kiểm tra trước rồi mới lưu để tránh lấy cùng một phần tử hai lần.

### 7. Trường hợp không có cặp phù hợp

`return []` là nhánh dự phòng sau vòng lặp. Theo giả thiết bài toán luôn có một đáp án, hàm sẽ trả về cặp chỉ số ngay trong vòng lặp.

## Ví dụ chạy từng bước

Với `nums = [3, 2, 4]` và `target = 6`, ban đầu `seen = {}`:

| Chỉ số `i` | Giá trị `x` | Số cần tìm | Xử lý |
| --- | --- | --- | --- |
| 0 | 3 | 3 | Chưa có, lưu `{3: 0}` |
| 1 | 2 | 4 | Chưa có, lưu `{3: 0, 2: 1}` |
| 2 | 4 | 2 | Tìm thấy số `2` ở chỉ số `1`, trả về `[1, 2]` |

## Lưu ý

- Trả về chỉ số, không phải giá trị.
- Kiểm tra trước khi lưu để không dùng cùng một phần tử hai lần.
- Với `[3, 3]` và `target = 6`, số `3` thứ hai tìm thấy số `3` thứ nhất, nên trả về `[0, 1]`.
- Thuật toán xử lý được số âm và số `0`.

## Độ phức tạp

- **Thời gian trung bình:** `O(n)`. Duyệt mảng một lần, mỗi thao tác tra cứu hoặc thêm dictionary có thời gian trung bình `O(1)`.
- **Bộ nhớ phụ:** `O(n)` để lưu dictionary.

## Cách giải khác: Duyệt từng cặp

Dùng hai vòng lặp để thử từng cặp `i`, `j`, với `j > i`. Nếu tổng bằng `target`, trả về `[i, j]`.

```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

- **Thời gian:** `O(n²)`.
- **Bộ nhớ phụ:** `O(1)`.
- Cách này chưa đáp ứng yêu cầu mở rộng.

## Cách chạy trên máy

File `Two_sum.py` có phần chạy thử ở cuối, nằm ngoài lớp `Solution`:

```python
if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
```

`if __name__ == "__main__":` giúp các ví dụ chỉ chạy khi thực thi file trực tiếp. Khi nộp trên LeetCode, chỉ cần chép phần `class Solution(object)` và hàm `twoSum`.

Từ thư mục `LeetCodeWithMe`, chạy:

```powershell
py .\Day1\Two_sum.py
```

Kết quả:

```text
[0, 1]
[1, 2]
[0, 1]
```
