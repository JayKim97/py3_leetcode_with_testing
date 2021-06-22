# https://leetcode.com/problems/linked-list-cycle/
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        checked = set()
        while head:
            if head in checked:
                return True
            checked.add(head)
            head = head.next
        return False


def set_up(arr, loop):
    if arr == []:
        return ListNode(None)
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    if loop >= 0:
        loop_node = head
        for i in range(loop):
            loop_node = loop_node.next
        temp.next = loop_node
    return head


class TestIntersect(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(Solution().hasCycle(set_up([], -1)), False)

    def test_no_circle(self):
        self.assertEqual(Solution().hasCycle(set_up([1, 2, 3], -1)), False)

    def test_circle(self):
        self.assertEqual(Solution().hasCycle(set_up([3, 2, 0, -4], 0)), True)
        self.assertEqual(Solution().hasCycle(set_up([1, 2, 3], 2)), True)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
