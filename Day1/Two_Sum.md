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

Đoạn code dưới đây có thể nộp trực tiếp trên LeetCode:

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Lưu giá trị -> chỉ số của các số đã gặp
        seen = {}

        for i, x in enumerate(nums):
            # Tính số còn thiếu để đạt tổng mục tiêu
            needed = target - x

            if needed in seen:
                return [seen[needed], i]

            # Kiểm tra trước, lưu sau để tránh dùng lại chính phần tử này
            seen[x] = i

        return []
```

## Giải thích code

- `class Solution`: Lớp chứa lời giải theo cấu trúc của LeetCode.
- `seen = {}`: Tạo dictionary lưu các giá trị và chỉ số đã gặp. Ví dụ `{3: 0}` nghĩa là số `3` ở chỉ số `0`.
- `enumerate(nums)`: Lấy đồng thời chỉ số `i` và giá trị `x`.
- `needed = target - x`: Tính số cần tìm.
- `if needed in seen`: Kiểm tra số cần tìm đã xuất hiện trước đó hay chưa.
- `return [seen[needed], i]`: Trả về hai chỉ số tạo thành đáp án.
- `seen[x] = i`: Ghi nhớ phần tử hiện tại để dùng cho các lượt sau.
- `return []`: Nhánh dự phòng khi không có lời giải.

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
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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
