from typing import Optional
from trees_helpers import *


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "#".join(res)

    # Decodes your encoded data to tree.

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split("#")
        indx = 0

        def dfs():
            nonlocal indx
            if vals[indx] == "N":
                indx += 1
                return None

            node = TreeNode(int(vals[indx]))
            indx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


root = create_tree_from_list([1, 2, 3, None, None, 4, 5])

serialized = Codec().serialize(root)
print(serialized)
deserialized = Codec().deserialize(serialized)
print_tree(deserialized)
