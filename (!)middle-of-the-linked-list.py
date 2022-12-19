# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val1=head
        val2=head
        while val2 and val2.next:
            val1, val2 = val1.next, val2.next.next
        return val1
