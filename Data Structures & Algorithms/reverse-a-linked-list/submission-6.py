# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(cur:Optional[ListNode], prev:Optional[ListNode]) -> Optional[ListNode]:
            if cur is None:
                return prev

            next = cur.next
            cur.next = prev

            return helper(next, cur)

        return helper(head, None)
        