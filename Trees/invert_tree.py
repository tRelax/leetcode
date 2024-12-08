# Definition for a binary tree node.
from typing import Optional
from trees_helpers import *


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return None

        root.left, root.right = self.helper(root.right), self.helper(root.left)

        return root


print_tree(Solution().invertTree(create_tree_from_list([1, 2, 3, 4, 5, 6, 7])))
print_tree(Solution().invertTree(create_tree_from_list([3, 2, 1])))
