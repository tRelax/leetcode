from trees_helpers import *


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root and root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root and root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


root = create_tree_from_list([5, 3, 8, 1, 4, 7, 9, None, 2])

print(Solution().lowestCommonAncestor(root, TreeNode(3), TreeNode(8)))

root = create_tree_from_list([5, 3, 8, 1, 4, 7, 9, None, 2])

print(Solution().lowestCommonAncestor(root, TreeNode(3), TreeNode(4)))
