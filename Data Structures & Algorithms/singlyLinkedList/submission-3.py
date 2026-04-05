class Node:
    def __init__(self, val: int):
        self.value = val
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
            if i == index:
                return cur.value
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
        cur = self.head.next
        prev = self.head
        i = 0 
        while cur:
            if i == index:
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                return True
            prev = cur 
            cur = cur.next
            i += 1
        return False
        
    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next

        while cur:
            res.append(cur.value)
            cur = cur.next
        return res
        
