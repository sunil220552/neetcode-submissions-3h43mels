"""
* Add new element to the tail 
* Remove it from the head
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):

        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        print(self.head.next == self.tail)
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        node = ListNode(value) 

        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

        

    def appendleft(self, value: int) -> None:

        node = ListNode(value)
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.tail.prev.val
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        val = self.head.next.val

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next 
        return val

        
