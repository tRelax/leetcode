from typing import Optional
from trees_helpers import *

# DFS recursive


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = create_tree_from_list([1, 2, 3, None, None, 4])
print_tree(root)
print(Solution().maxDepth(root))
