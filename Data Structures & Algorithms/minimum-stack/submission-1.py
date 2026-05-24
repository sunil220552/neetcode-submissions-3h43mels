class MinStack:
    def __init__(self):
        self._st = []
        self._minSt = []
        
    def push(self, val: int) -> None:
        self._st.append(val)

        if not self._minSt:
            self._minSt.append(val)
        else:
            if val <= self._minSt[-1]:
                self._minSt.append(val)
        
    def pop(self) -> None:
        val = self._st.pop()

        if self._minSt[-1] == val:
            self._minSt.pop()
        
    def top(self) -> int:
        return self._st[-1]
        
    def getMin(self) -> int:
        return self._minSt[-1]
        
