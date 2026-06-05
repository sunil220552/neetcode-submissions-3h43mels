# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        head = res


        while lists:
            tmp = []
            node = ListNode(float('inf'))

            for n in lists:
                if n:
                    if n.val < node.val:
                        node = n

            print(node.val)
                        
            res.next = node
            res = res.next
            for n in lists:
                if n == node:
                    n = n.next
                if n:
                    tmp.append(n)
            lists = tmp

        return head.next


        