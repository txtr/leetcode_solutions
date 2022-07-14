class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def key_func(x: (int, int)) -> int:
            return x[0]
        
        new_nums = []
        
        for i in range(len(nums)):
            new_nums.append((nums[i], i))
        
        new_nums.sort(key = key_func)
        
        i = 0
        j = len(new_nums) - 1
        while i < j:
            x = new_nums[i][0]
            y_req = target - x
            y = new_nums[j][0]
            
            if y_req < y:
                j = j - 1
            elif y_req > y:
                i = i + 1
            elif y_req == y:
                return [new_nums[i][1], new_nums[j][1]]