#Defination of Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Timepass:
    def isSameTree(self, p, q):

        if p is None and q is None:
            return True


        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.left.left = TreeNode(4)
obj = Timepass()
print(obj.isSameTree(p, q))
