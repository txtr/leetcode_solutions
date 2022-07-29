class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_horizontal_slice = 0
        max_vertical_slice = 0
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        for index, horizontalCut in enumerate(horizontalCuts):
            if index == 0:
                continue
            elif horizontalCut <= h and horizontalCuts[index] - horizontalCuts[index - 1] > max_horizontal_slice:
                max_horizontal_slice = horizontalCuts[index] - horizontalCuts[index - 1]
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        for index, verticalCut in enumerate(verticalCuts):
            if index == 0:
                continue
            elif verticalCut <= w and verticalCuts[index] - verticalCuts[index - 1] > max_vertical_slice:
                max_vertical_slice = verticalCuts[index] - verticalCuts[index - 1]
        max_horizontal_slice = max_horizontal_slice % (1000000007)
        max_vertical_slice = max_vertical_slice % (1000000007)
        
        return (max_horizontal_slice * max_vertical_slice) % (1000000007)
            