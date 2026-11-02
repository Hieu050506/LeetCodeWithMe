# 2. Add Two Numbers — Cộng hai số

**Độ khó:** Trung bình (Medium)

## Đề bài

Cho hai danh sách liên kết không rỗng `l1` và `l2`, biểu diễn hai số nguyên không âm. Mỗi nút chứa một chữ số, các chữ số được lưu theo thứ tự đảo ngược.

Hãy cộng hai số và trả về kết quả dưới dạng một danh sách liên kết cũng lưu các chữ số theo thứ tự đảo ngược.

Hai số không có chữ số `0` ở đầu, ngoại trừ chính số `0`.

### Ví dụ 1

```text
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
```

Giải thích: `[2, 4, 3]` biểu diễn `342`, `[5, 6, 4]` biểu diễn `465`. Vì `342 + 465 = 807`, kết quả là `[7, 0, 8]`.

### Ví dụ 2

```text
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Ví dụ 3

```text
Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]
```

Giải thích: `9 999 999 + 9 999 = 10 009 998`.

### Ràng buộc

- Số nút của mỗi danh sách nằm trong khoảng `[1, 100]`.
- `0 <= Node.val <= 9`.
- Danh sách biểu diễn một số không có chữ số `0` ở đầu, ngoại trừ số `0`.

## Danh sách liên kết là gì?

Mỗi nút có hai thành phần:

- `val`: Chữ số tại nút hiện tại.
- `next`: Tham chiếu đến nút tiếp theo. Nút cuối có `next = None`.

```text
l1 → [2] → [4] → [3] → None
l2 → [5] → [6] → [4] → None
```

`l1` và `l2` là tham chiếu đến nút đầu, không phải danh sách Python. Cách viết `[2, 4, 3]` trong ví dụ là cách biểu diễn ngắn gọn các giá trị của chuỗi nút.

Vì hàng đơn vị đứng đầu, ta có thể cộng ngay từ nút đầu theo cách cộng có nhớ thông thường.

## Thuật toán giải quyết

**Đầu vào:**

- `l1`: Nút đầu của danh sách liên kết biểu diễn số thứ nhất.
- `l2`: Nút đầu của danh sách liên kết biểu diễn số thứ hai.

**Đầu ra:**

- Nút đầu của danh sách liên kết biểu diễn tổng, với các chữ số theo thứ tự đảo ngược.

### Các bước thực hiện:

1. Tạo nút giả `dummy = ListNode(0)` và đặt `current = dummy`.
2. Khởi tạo số nhớ `carry = 0`.
3. Lặp khi `l1` còn nút, `l2` còn nút hoặc vẫn còn số nhớ.
4. Lấy chữ số hiện tại của mỗi danh sách; nếu danh sách đã hết thì dùng `0`.
5. Tính `total = x + y + carry`.
6. Lấy chữ số kết quả bằng `total % 10` và cập nhật số nhớ bằng `total // 10`.
7. Tạo nút chứa chữ số kết quả, nối vào cuối danh sách và di chuyển `current`.
8. Di chuyển `l1` và `l2` sang nút tiếp theo nếu còn nút.
9. Trả về `dummy.next`, tức là nút đầu của kết quả.

## Code Python

Đoạn code sau dùng mẫu `class Solution(object)` và có thể chép vào phần lời giải trên LeetCode. LeetCode cung cấp sẵn lớp `ListNode`; file [Add_two_numbers.py](Add_two_numbers.py) có thêm định nghĩa lớp này để chạy trên máy.

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            total = x + y + carry
            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next
```

## Giải thích code

### 1. `self`, `l1`, `l2` là gì?

- `self`: Đối tượng `Solution` đang gọi hàm; Python tự truyền tham số này.
- `l1`: Nút đang xét trong danh sách thứ nhất. Ban đầu là nút đầu.
- `l2`: Nút đang xét trong danh sách thứ hai. Ban đầu là nút đầu.

Khi gọi `solution.addTwoNumbers(l1, l2)`, bạn chỉ truyền hai danh sách liên kết. Hàm trả về một nút đầu `ListNode`, không trả về chỉ số như bài Two Sum.

### 2. Nút giả `dummy` và con trỏ `current`

`dummy = ListNode(0)` tạo nút giả để việc nối các nút kết quả thuận tiện ngay từ đầu. `current = dummy` cho hai biến cùng tham chiếu đến nút này.

`dummy` được giữ lại để biết điểm bắt đầu. `current` di chuyển dần đến nút cuối sau mỗi lượt. Giá trị `0` của nút giả không thuộc kết quả, nên cuối hàm trả về `dummy.next`.

### 3. Điều kiện vòng lặp

`while l1 is not None or l2 is not None or carry:` nghĩa là tiếp tục cộng nếu còn ít nhất một danh sách chưa hết hoặc còn số nhớ.

Điều kiện `or carry` xử lý trường hợp như `9 + 1 = 10`: sau khi hai danh sách đều hết, cần tạo thêm nút `1` để trả về `[0, 1]`.

### 4. Lấy chữ số hiện tại

`x = l1.val if l1 is not None else 0` lấy giá trị nút hiện tại của danh sách thứ nhất; nếu đã hết thì dùng `0`. Dòng lấy `y` hoạt động tương tự.

Nhờ vậy, hai danh sách có thể có độ dài khác nhau.

### 5. Cộng và xử lý số nhớ

- `total = x + y + carry`: Tổng hai chữ số và số nhớ từ lượt trước.
- `digit = total % 10`: Phần dư khi chia cho `10`, là chữ số cần lưu.
- `carry = total // 10`: Phần nguyên khi chia cho `10`, là số nhớ cho lượt tiếp theo.

Ví dụ `total = 14` thì `digit = 4` và `carry = 1`. Số nhớ luôn là `0` hoặc `1` vì tổng lớn nhất là `9 + 9 + 1 = 19`.

### 6. Nối nút mới

`current.next = ListNode(digit)` tạo và nối một nút chứa chữ số vừa tính. `current = current.next` di chuyển đến nút mới để chuẩn bị nối tiếp.

### 7. Di chuyển sang chữ số tiếp theo

Nếu `l1` chưa hết, `l1 = l1.next` chuyển sang nút kế tiếp. Tương tự với `l2`. Chỉ di chuyển khi nút hiện tại khác `None` để tránh truy cập `.next` của `None`.

## Ví dụ chạy từng bước

Với `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]`, ban đầu `carry = 0`:

| Lượt | `x` | `y` | Nhớ đầu lượt | `total` | `digit` | Nhớ mới | Kết quả đã tạo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 5 | 0 | 7 | 7 | 0 | `[7]` |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 | `[7, 0]` |
| 3 | 3 | 4 | 1 | 8 | 8 | 0 | `[7, 0, 8]` |

Hai danh sách đều hết và số nhớ bằng `0`, vòng lặp dừng. `dummy.next` trỏ đến chuỗi `7 → 0 → 8 → None`, biểu diễn số `807`.

## Độ phức tạp

Gọi `m` và `n` là số nút của hai danh sách:

- **Thời gian:** `O(max(m, n))`, vì mỗi nút đầu vào được xét một lần và có thể thêm một lượt cho số nhớ cuối.
- **Bộ nhớ cho kết quả:** `O(max(m, n))` nút.
- **Bộ nhớ phụ ngoài kết quả:** `O(1)`.

## Cách chạy trên máy

Từ thư mục `LeetCodeWithMe`, chạy:

```powershell
py .\Day1\Add_two_numbers.py
```

Kết quả:

```text
[7, 0, 8]
[0]
[8, 9, 9, 9, 0, 0, 0, 1]
```

File Python có các phần hỗ trợ chạy thử:

- `ListNode`: Định nghĩa một nút liên kết.
- `build_linked_list`: Chuyển danh sách Python thành danh sách liên kết.
- `linked_list_to_list`: Đọc các nút thành danh sách Python để in ra màn hình.
- `if __name__ == "__main__":`: Chạy ba ví dụ khi thực thi file trực tiếp.

Khi nộp trên LeetCode, chỉ cần chép phần `class Solution(object)` cùng hàm `addTwoNumbers` trong mục Code Python.
