class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        while result and result[-1] == "null":
            result.pop()

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root


codec = Codec()

root = codec.deserialize("1,2,3,null,null,4,5")
print(codec.serialize(root))

root2 = codec.deserialize("")
print(codec.serialize(root2))