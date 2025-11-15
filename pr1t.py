class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


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


p1 = build_tree([1,2,3])
q1 = build_tree([1,2,3])
print(isSameTree(p1, q1))

p2 = build_tree([1,2])
q2 = build_tree([1,None,2])
print(isSameTree(p2, q2))

p3 = build_tree([1,2,1])
q3 = build_tree([1,1,2])
print(isSameTree(p3, q3))