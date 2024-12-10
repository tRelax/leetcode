from typing import List, Optional
from trees_helpers import *


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    lvl.append(node.val)

            if lvl:
                res.append(lvl[-1])

        return res


root = create_tree_from_list([1, 2, 3])
print(Solution().rightSideView(root))

root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
print(Solution().rightSideView(root))

root = create_tree_from_list([1, 2])
print(Solution().rightSideView(root))

root = create_tree_from_list([1, 2, 3, 4])
print(Solution().rightSideView(root))
