# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nod1=ListNode(0)
        curr=nod1
        tmp=0
        while l1 or l2:
            val = tmp
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            tmp, val = divmod(val, 10)
            curr.next = ListNode(val)
            curr = curr.next
        if tmp == 1:
            curr.next = ListNode(1)
        return nod1.next
