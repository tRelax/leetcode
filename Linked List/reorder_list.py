from typing import Optional
from linked_list_helpers import *


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second part reversed
        second = slow.next
        slow.next = prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge first and second part
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        print_linked_list(head)


head = create_linked_list([2, 4, 6, 8])
print(Solution().reorderList(head))
