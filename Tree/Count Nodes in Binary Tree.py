class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root):

        if root is None:
            return 0

        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)


        return 1 + left_count + right_count



#  Create Tree
#     1
#    / \
#   2   3
#  / \
# 4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


obj = Solution()
print(obj.countNodes(root))