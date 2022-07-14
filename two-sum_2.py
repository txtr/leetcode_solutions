class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index in range(len(nums)):
            try:
                x = nums[index]
                y = target - x
                return [hash_map[y], index]
            except KeyError:
                hash_map[nums[index]] = index