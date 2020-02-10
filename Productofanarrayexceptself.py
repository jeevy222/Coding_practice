class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        L, R, answer = [0] * l, [0] * l, [0] * l
        L[0] = R[l - 1] = 1
        for i in range(1, l):
            L[i] = L[i - 1] * nums[i - 1]
        for i in reversed(range(l - 1)):
            R[i] = R[i + 1] * nums[i + 1]
        for i in range(l):
            answer[i] = L[i] * R[i]
        return (answer)
