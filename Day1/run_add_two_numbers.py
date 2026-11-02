# -*- coding: utf-8 -*-
import Add_two_numbers as solution_code


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Cung cấp lớp nút cho lời giải khi chạy trên máy.
# Trên LeetCode, hệ thống cung cấp ListNode sẵn.
solution_code.ListNode = ListNode


def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


if __name__ == "__main__":
    solution = solution_code.Solution()
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
