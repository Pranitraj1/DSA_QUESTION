class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if node is None:
                return


            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
sol = Solution()
print(sol.preorderTraversal(root))