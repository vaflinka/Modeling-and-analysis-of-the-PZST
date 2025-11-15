class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root):
        self.cameras = 0

        def dfs(node):
            if not node:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 2 or right == 2:
                self.cameras += 1
                return 0

            if left == 0 or right == 0:
                return 1

            return 2

        if dfs(root) == 2:
            self.cameras += 1

        return self.cameras


root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)

print(Solution().minCameraCover(root))  

root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.left.left = TreeNode(0)

print(Solution().minCameraCover(root))  