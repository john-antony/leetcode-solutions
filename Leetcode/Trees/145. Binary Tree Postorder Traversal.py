# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive approach 

        # res = []

        # def postorder(root):
        #     if not root:
        #         return [] 
        #     postorder(root.left)
        #     postorder(root.right)
        #     res.append(root.val)

        # postorder(root)
    
        # return res

        # iterative approach

        res = [] 
        stack = [root]
        visit = [False]

        while stack:
            curr, visited  = stack.pop(), visit.pop()
            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        
        return res