from typing import Optional
from linked_list_helpers import *


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        leftover = 0
        while l1 or l2 or leftover:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + leftover
            leftover = val // 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return dummy.next


l1 = create_linked_list([1, 2, 3])
l2 = create_linked_list([4, 5, 6])
Solution().addTwoNumbers(l1, l2)

l1 = create_linked_list([9])
l2 = create_linked_list([9])
Solution().addTwoNumbers(l1, l2)
l1 = create_linked_list([0])
l2 = create_linked_list([0])
Solution().addTwoNumbers(l1, l2)
