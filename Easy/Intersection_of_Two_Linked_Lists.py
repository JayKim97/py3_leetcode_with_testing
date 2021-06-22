# https://leetcode.com/problems/intersection-of-two-linked-lists/
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pt1 = headA
        pt2 = headB
        pt1_len, pt1end = self.get_len(headA)
        pt2_len, pt2end = self.get_len(headB)
        if pt1end != pt2end:
            return None

        if pt1_len < pt2_len:
            for i in range(pt2_len - pt1_len):
                pt2 = pt2.next
        else:
            for i in range(pt1_len - pt2_len):
                pt1 = pt1.next

        while pt1 and pt2:
            if pt1 == pt2:
                return pt1
            pt1 = pt1.next
            pt2 = pt2.next

    def get_len(self, pointer):
        num = 1
        while pointer:
            pointer = pointer.next
            num += 1
        end = pointer
        return num, end


def set_up(arrA, arrB, arrC):
    if arrA != []:
        headA = ListNode(arrA[0])
        tempA = headA
        for a in arrA[1:]:
            tempA.next = ListNode(a)
            tempA = tempA.next
    else:
        headA = ListNode(None)
        tempA = headA
    if arrA != []:
        headB = ListNode(5)
        tempB = headB
        for b in arrB[1:]:
            tempB.next = ListNode(b)
            tempB = tempB.next
    else:
        headB = ListNode(None)
        tempB = headB

    conC = ListNode(arrC[0])
    tempC = conC
    for c in arrC[1:]:
        tempC.next = ListNode(c)
        tempC = tempC.next
    tempA.next = conC if tempA.val else None
    tempB.next = conC if tempB.val else None
    return headA, headB, conC


class TestIntersect(unittest.TestCase):
    def test_empty(self):
        headA, headB, _ = set_up([], [1, 2, 3], [4, 5])
        self.assertEqual(Solution().getIntersectionNode(headA, headB), None)
        self.assertEqual(Solution().getIntersectionNode(
            ListNode(None), ListNode(None)), None)

    def test_intersect(self):
        # same length
        headA, headB, con = set_up([1, 2, 3], [4, 5, 6], [7, 8, 9])
        self.assertEqual(Solution().getIntersectionNode(headA, headB), con)
        # longer headA
        headA, headB, con = set_up([1, 2, 3, 4], [5, 6], [7, 8, 9])
        self.assertEqual(Solution().getIntersectionNode(headA, headB), con)
        # longer headB
        headA, headB, con = set_up([1, 2], [3, 4, 5, 6], [7, 8, 9])
        self.assertEqual(Solution().getIntersectionNode(headA, headB), con)


def main():
    # headA, headB = set_up([4, 1], [5, 6, 1], [8, 4, 5])
    # sol = Solution()
    # print(sol.getIntersectionNode(headA, headB).val)
    unittest.main()


if __name__ == "__main__":
    main()
