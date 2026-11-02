# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def build_linked_list(values):
    """Tạo danh sách liên kết từ một danh sách Python."""
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    """Đọc các chữ số trong danh sách liên kết để in kết quả."""
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


if __name__ == "__main__":
    solution = Solution()
    examples = [
        ([2, 4, 3], [5, 6, 4]),
        ([0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
    ]

    for first, second in examples:
        l1 = build_linked_list(first)
        l2 = build_linked_list(second)
        result = solution.addTwoNumbers(l1, l2)
        print(linked_list_to_list(result))
