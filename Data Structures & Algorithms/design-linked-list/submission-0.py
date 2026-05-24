class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self._st, self._en = ListNode(), ListNode()
        self._st.next, self._en.prev = self._en, self._st
        

    def get(self, index: int) -> int:
        i = 0
        node = self._st.next

        while node and node != self._en:
            if i == index:
                return node.val
            i += 1
            node = node.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        head = self._st.next

        self._st.next, head.prev = node, node
        node.prev, node.next = self._st, head 
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        prev_node = self._en.prev

        prev_node.next, self._en.prev = node, node
        node.prev, node.next = prev_node, self._en
        

    def addAtIndex(self, index: int, val: int) -> None:
        # st <-> 0 <-> 2 <-> end
        new_node = ListNode(val)
        i = 0
        node = self._st.next

        while node and node != self._en:
            if i == index:
                prev_node = node.prev

                prev_node.next, node.prev = new_node, new_node
                new_node.prev, new_node.next = prev_node, node
                return

            i += 1
            node = node.next

        if node == self._en:
            self.addAtTail(val)
        

    def deleteAtIndex(self, index: int) -> None:

        i = 0
        node = self._st.next

        while node and node != self._en:
            if i == index:
                p, n = node.prev, node.next
                p.next = n
                n.prev = p
            i += 1
            node = node.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)