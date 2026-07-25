# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 使用迭代法（栈）进行中序遍历，比递归更节省空间且不易爆栈
        stack = []
        curr = root
        count = 0
        
        while curr or stack:
            # 1. 一路向左，将沿途节点压入栈
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. 弹出栈顶节点（这就是当前最小的节点）
            curr = stack.pop()
            count += 1
            
            # 3. 如果找到了第 k 个节点，直接返回值
            if count == k:
                return curr.val
            
            # 4. 转向右子树
            curr = curr.right
            
        return -1  # 理论上如果 k 合法，不会执行到这里



        