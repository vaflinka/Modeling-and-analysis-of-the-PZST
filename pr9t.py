class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal):
        i = 0
        n = len(traversal)
        stack = []

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            node = TreeNode(value)

            while len(stack) > depth:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]


from collections import deque

def tree_to_level_array(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


sol = Solution()

root1 = sol.recoverFromPreorder("1-2--3--4-5--6--7")
print(tree_to_level_array(root1))

root2 = sol.recoverFromPreorder("1-2--3---4-5--6---7")
print(tree_to_level_array(root2))

root3 = sol.recoverFromPreorder("1-401--349---90--88")
print(tree_to_level_array(root3))