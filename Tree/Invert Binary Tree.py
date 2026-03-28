# Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        # swap
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# 🔎 Create Tree
#     4
#    / \
#   2   7

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# 🔎 Invert Tree
sol = Solution()
new_root = sol.invertTree(root)


# 🔎 Simple print (preorder)
def printTree(node):
    if node:
        print(node.val, end=" ")
        printTree(node.left)
        printTree(node.right)


printTree(new_root)