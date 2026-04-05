class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        dummy = Node(-1)
        self.head = dummy
        self.tail = dummy

    def get(self, index: int) -> int:
        cur = self.head.next 
        i = 0
        while cur:
            if index == i:
                return cur.val
            cur = cur.next
            i += 1
        return -1 
            
    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        if self.head == self.tail:
            self.tail = node
        self.head.next = node
        
    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        prev = self.head
        cur = self.head.next
        i = 0 
        while cur:
            if index == i:
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                    self.tail.next = None
                return True
            i += 1
            prev = cur
            cur = cur.next
        return False

    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
