# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 边界条件：如果子树为空，任何树都包含空树
        if not subRoot:
            return True
        # 边界条件：如果主树为空但子树不为空，肯定不包含
        if not root:
            return False

        # 1. 使用 BFS 遍历主树 root 的每一个节点
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            # 2. 如果当前节点的值与子树根节点的值相同，则去比较这两棵树是否完全一样
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            
            # 3. 将当前节点的左右子节点加入队列，继续遍历
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        # 4. 遍历完整个主树都没找到，返回 False
        return False

    # 辅助函数：判断两棵树是否完全相同
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
