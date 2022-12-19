# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        [begin, end] = self.reverseListRecu(head)
        return begin
    def reverseListRecu(self, head):
        if not head:
            return [None, None]
        [begin, end] = self.reverseListRecu(head.next)
        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]
