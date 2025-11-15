class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def build_tree(arr):
    if not arr:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_to_array(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


r1 = build_tree([4,2,7,1,3,6,9])
print(tree_to_array(invertTree(r1)))

r2 = build_tree([2,1,3])
print(tree_to_array(invertTree(r2)))

r3 = build_tree([])
print(tree_to_array(invertTree(r3)))