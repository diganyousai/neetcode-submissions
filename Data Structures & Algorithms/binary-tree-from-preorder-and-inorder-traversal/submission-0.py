# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 1. 递归终止条件：如果前序或中序列表为空，说明没有节点了，返回 None
        if not preorder or not inorder:
            return None
        
        # 2. 确定根节点：前序遍历的第一个元素永远是当前子树的根
        root = TreeNode(preorder[0])
        
        # 3. 在中序遍历中找到根节点的索引
        # 这个索引将中序数组分成了“左子树部分”和“右子树部分”
        mid = inorder.index(preorder[0])
        
        # 4. 递归构建左子树
        # 前序部分：从第2个元素开始，取 mid 个长度（对应左子树的节点数）
        # 中序部分：从开头到 mid 之前
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # 5. 递归构建右子树
        # 前序部分：从 mid+1 开始直到结束
        # 中序部分：从 mid+1 开始直到结束
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root
        