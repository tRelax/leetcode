# Definition for singly-linked list.
from typing import Optional
from linked_list_helpers import *


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = res = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2
        return res.next


values1 = [1, 2, 4]
values2 = [1, 3, 5]
list1 = create_linked_list(values1)
list2 = create_linked_list(values2)

print_linked_list(list1)
print_linked_list(list2)

sol = Solution().mergeTwoLists(list1, list2)
print_linked_list(sol)
