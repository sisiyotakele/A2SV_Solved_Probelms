# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        curr1 = l1
        curr2 = l2

        while curr1:
            stack1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next

        carry = 0
        head = None

        while stack1 or stack2 or carry:

            total = carry

            if stack1:
                total += stack1.pop()

            if stack2:
                total += stack2.pop()

            carry = total // 10
            digit = total % 10

            node = ListNode(digit)

            node.next = head
            head = node

        return head