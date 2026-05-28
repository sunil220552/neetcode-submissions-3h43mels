# I'll use a doubly linked list to implement this solution. 
# head <-> v1 <-> v2 <-> v3 <-> tail

class ListNode:
    def __init__(self, url:str):
        self.url = url
        self.prev, self.next = None, None

class BrowserHistory:

    def __init__(self, homepage: str):
        self._head, self._tail = ListNode("head"), ListNode("tail")
        self._head.next, self._tail.prev = self._tail, self._head
        self._cur = self._head
        self.visit(homepage)
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        # cur <-> next
        # cur <->  node <-> self._tail
        cur = self._cur
        cur.next, self._tail.prev = node, node
        node.prev, node.next = cur, self._tail
        self._cur = node


    def back(self, steps: int) -> str:

        while self._cur.prev != self._head and steps > 0:
            self._cur = self._cur.prev
            steps -= 1

        return self._cur.url

    def forward(self, steps: int) -> str:
        while self._cur.next != self._tail and steps > 0:
            self._cur = self._cur.next
            steps -= 1

        return self._cur.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)