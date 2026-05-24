class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for op in operations:
            if op == "+":
                sc = st[-1] + st[-2]
                st.append(sc)
            elif op == "D":
                st.append(2 * st[-1])
            elif op == "C":
                st.pop()
            else:
                st.append(int(op))

        return sum(st)
        