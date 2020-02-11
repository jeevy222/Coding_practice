class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if (nums == None or len(nums) < 3):
            return (-1)
        result = nums[0] + nums[1] + nums[2]
        length = len(nums)
        for i in range(length - 2):
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                sums = nums[i] + nums[j] + nums[k]
                if (abs(sums - target) < abs(result - target)):
                    result = sums
                if (sums > target):
                    k -= 1
                else:
                    j += 1

        return result
