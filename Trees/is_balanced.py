from typing import Optional
from trees_helpers import *


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


print(Solution().isBalanced(create_tree_from_list([1, 2, 3, None, None, 4])))
print(Solution().isBalanced(create_tree_from_list(
    [1, 2, 3, None, None, 4, None, 5])))
