from typing import Optional

from trees_helpers import *


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root, subtree):
        if not root and not subtree:
            return True
        elif root and subtree and root.val == subtree.val:
            return self.isSame(root.left, subtree.left) and self.isSame(root.right, subtree.right)
        else:
            return False


print(Solution().isSubtree(create_tree_from_list(
    [1, 2, 3, 4, 5]), create_tree_from_list([2, 4, 5])))

print(Solution().isSubtree(create_tree_from_list(
    [1, 2, 3, 4, 5, None, None, 6]), create_tree_from_list([2, 4, 5])))
