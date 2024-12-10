from typing import List, Optional
from trees_helpers import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            cur_lvl = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    cur_lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if cur_lvl:
                res.append(cur_lvl)

        return res


root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
print(Solution().levelOrder(root))

root = create_tree_from_list([1])
print(Solution().levelOrder(root))

root = create_tree_from_list([])
print(Solution().levelOrder(root))
