class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.ans = -10**15

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.ans = max(self.ans, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return self.ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().maxPathSum(root))  

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().maxPathSum(root))  