# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if head == None or head.next == None:
            return head

        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            fast, slow, prev = fast.next.next, slow.next, slow
        current, prev.next, prev = slow, None, None

        while current != None:
            current.next, prev, current = prev, current, current.next

        l1, l2 = head, prev
        dummy = ListNode(0)
        current = dummy

        while l1 != None and l2 != None:
            current.next, current, l1 = l1, l1, l1.next
            current.next, current, l2 = l2, l2, l2.next

        return dummy.next
