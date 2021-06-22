import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.val is None:
            return False
        if head.next == None:
            return True
        pt1 = pt2 = head
        # find half point
        while pt1 and pt1.next:
            pt1 = pt1.next.next
            pt2 = pt2.next

        # fill the stack with 2nd half
        stack = []
        while pt2:
            stack.append(pt2)
            pt2 = pt2.next

        while stack:
            if head.val != stack.pop().val:
                return False
            head = head.next
        return True


def set_up(arr):
    if arr == []:
        return ListNode(None)
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
    return head


class TestIntersect(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Solution().isPalindrome(set_up([])), False)

    def test_single(self):
        self.assertEqual(Solution().isPalindrome(set_up([1])), True)

    def test_double(self):
        self.assertEqual(Solution().isPalindrome(set_up([1, 1])), True)
        self.assertEqual(Solution().isPalindrome(set_up([1, 0])), False)

    def test_palindrome(self):
        self.assertEqual(Solution().isPalindrome(
            set_up([1, 2, 3, 4, 3, 2, 1])), True)
        self.assertEqual(Solution().isPalindrome(
            set_up([1, 2, 3, 4, 4, 3, 2, 1])), True)
        self.assertEqual(Solution().isPalindrome(set_up([1, 2, 3, 4])), False)
        self.assertEqual(Solution().isPalindrome(
            set_up([1, 2, 3, 4, 5])), False)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
