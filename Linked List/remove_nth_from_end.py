from typing import Optional
from linked_list_helpers import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

head = create_linked_list([1,2,3,4])
n = 2
#head = create_linked_list([1])
#n = 1

print_linked_list(Solution().removeNthFromEnd(head, n)) # [1,2,4]