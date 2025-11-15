class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    stack = []
    curr = root
    while True:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right


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


root1 = build_tree([3,1,4,None,2])
print(kthSmallest(root1, 1))

root2 = build_tree([5,3,6,2,4,None,None,1])
print(kthSmallest(root2, 3))