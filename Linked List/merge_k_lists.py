from typing import List, Optional
from linked_list_helpers import *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # -2000 because values are -1000 < list[i][j] < 1000
        node = res = ListNode(-2000)

        for l in lists:
            tmpdummy = dummy = ListNode()
            accList = node
            while accList and l:
                if accList.val <= l.val:
                    tmpdummy.next = accList
                    accList = accList.next
                else:
                    tmpdummy.next = l
                    l = l.next
                tmpdummy = tmpdummy.next
            tmpdummy.next = accList or l
            node = dummy.next
        print_linked_list(res.next)
        return res.next


lists = [create_linked_list([-1, 2, 4]), create_linked_list(
    [1, 3, 5]), create_linked_list([3, 6])]
Solution().mergeKLists(lists)

Solution().mergeKLists([create_linked_list([])])
