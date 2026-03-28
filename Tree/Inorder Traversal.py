# Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# 🔎 Test
sol = Solution()
print(sol.inorderTraversal(root))  # Output: [1,3,2]

