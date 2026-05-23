class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_to_right = arr[-1]

        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = max_to_right 
            max_to_right = max(max_to_right, tmp)

        arr[-1] = -1
        return arr








        