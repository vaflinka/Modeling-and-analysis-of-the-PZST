class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)

    return mirror(root, root)


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


r1 = build_tree([1,2,2,3,4,4,3])
print(isSymmetric(r1))

r2 = build_tree([1,2,2,None,3,None,3])
print(isSymmetric(r2))

r3 = build_tree([1,2,1])
print(isSymmetric(r3))