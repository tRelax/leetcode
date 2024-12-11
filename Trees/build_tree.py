from typing import List, Optional
from trees_helpers import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid+1:])

        return root


print_tree(Solution().buildTree(preorder=[1, 2, 3, 4], inorder=[2, 1, 3, 4]))
