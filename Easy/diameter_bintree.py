# https://leetcode.com/problems/diameter-of-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        d, _ = self.diameter_height(root)
        return d

    def diameter_height(self, root):
        if root is None:
            return 0, 0
        ld, lh = self.diameter_height(root.left)
        rd, rh = self.diameter_height(root.right)
        return max(lh + rh, ld, rd), 1 + max(lh, rh)
