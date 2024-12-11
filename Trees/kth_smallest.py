from typing import Optional
from trees_helpers import *


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]


root = create_tree_from_list([4, 3, 5, 2, None])

print(Solution().kthSmallest(root, 4))
