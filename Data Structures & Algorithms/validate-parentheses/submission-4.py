class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c in "({[":
                st.append(c)
            else:
                if not st:
                    return False
                if c == ")":
                    if st[-1] != "(":
                        return False
                elif c == "}":
                    if st[-1] != "{":
                        return False
                else:
                    if st[-1] != "[":
                        return False
                st.pop()

        return True if not st else False


                
        