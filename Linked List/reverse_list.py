# Definition for singly-linked list.
from typing import Optional
from linked_list_helpers import ListNode, create_linked_list, print_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


values = [0, 1, 2, 3]
head = create_linked_list(values)

print("Original list:")
print_linked_list(head)

# Reverse the linked list
solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed list:")
print_linked_list(reversed_head)
