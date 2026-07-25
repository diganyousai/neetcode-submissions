# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            res = [[root]]
            l=0
            while res[l]: 
                s = res[l]
                m = []
                for i in s:
                    if i.left:
                        m.append(i.left)
                    if i.right:
                        m.append(i.right)
                if m != []:
                    res.append(m)
                else:
                    break
                l+=1
        for j in res:
            for k in range(len(j)):
                j[k]=j[k].val
        return res

                
        