# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        i, j = head, head
        while j and j.next:
            i = i.next
            j = j.next.next
        j, i.next = i.next, None
        prev = None
        while j:
            nxt = j.next
            j.next = prev
            prev = j
            j = nxt
        i, j = head, prev
        while j:
            a, b = i.next, j.next
            i.next = j
            j.next = a
            i, j = a, b
        