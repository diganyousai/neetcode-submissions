# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 两个都为空，说明遍历到了叶子节点之后，完全匹配
        if p is None and q is None:
            return True
        
        # 2. 只有一个为空，或者都不为空但值不相等，直接返回 False
        if p is None or q is None or p.val != q.val:
            return False
        
        # 3. 当前节点匹配，继续递归比较左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        