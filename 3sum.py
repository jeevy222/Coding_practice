class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)
        for i in range(length - 2):

            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                target = nums[i] + nums[j] + nums[k]
                if (nums[i] + nums[j] + nums[k] < 0):
                    j += 1
                elif (nums[i] + nums[j] + nums[k] > 0):
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while (j < k and nums[j] == nums[j + 1]):
                        j = j + 1
                    while (j < k and nums[k] == nums[k - 1]):
                        k = k - 1
                    j = j + 1
                    k = k - 1
        return result