from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = []

        for i in range(len(sandwiches)-1, -1, -1):
            st.append(sandwiches[i])

        queue = deque(students)

        while len(queue) > 0 and st[-1] in queue:

            if queue[0] == st[-1]:
                queue.popleft()
                st.pop()
            else:
                tmp = queue.popleft()
                queue.append(tmp)

        return len(queue)


        