class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s ={}
        for i, num in enumerate(nums):
            x =target - num
            if x in s:
                return [s[x],i]
            else:
                s[num] = i

        return []
