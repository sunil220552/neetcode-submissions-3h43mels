class ST:
    def __init__(self, s, e):
        self.st, self.en = s, e
        self.left , self.right = None, None

class MyCalendar:
    
    def __init__(self):
        self.root = None

    def _book(self, node, st : int, en : int) -> bool:
        if en <= node.st:
            if not node.left:
                node.left = ST(st, en)
                return True
            return self._book(node.left, st, en)

        elif st >= node.en:
            if not node.right:
                node.right = ST(st, en)
                return True
            return self._book(node.right, st, en)
        else:
            return False

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = ST(startTime, endTime)
            return True

        return self._book(self.root, startTime, endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)