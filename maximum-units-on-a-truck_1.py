class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def get_key(boxType: tuple) -> int:
            return boxType[1]
        
        boxTypes.sort(key = get_key)
        boxTypes.reverse()
        
        boxes = 0
        units = 0
        
        for boxType in boxTypes:
            if boxType[0] > (truckSize - boxes):
                units += (truckSize - boxes) * boxType[1]
                boxes += (truckSize - boxes)
                return units
            else:
                units += boxType[0] * boxType[1]
                boxes += boxType[0]
        return units