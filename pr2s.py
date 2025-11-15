class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


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


root1 = build_tree([1, None, 2, 3])
print(inorderTraversal(root1))

root2 = build_tree([])
print(inorderTraversal(root2))

root3 = build_tree([1])
print(inorderTraversal(root3))