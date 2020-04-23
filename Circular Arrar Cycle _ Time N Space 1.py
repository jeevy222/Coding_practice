'''We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

Example 1:

Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
Example 2:

Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1
Example 3:

Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.'''


def circularArrayLoop(self, nums):
    if not nums or len(nums) < 2: return False

    for i in xrange(len(nums)):

        if nums[i] == 0:
            continue
        if nums[i] > 0:
            direction = 1
        else:
            direction = -1
        flag = True  # check is the direction remains unchanged
        slow, fast = i, (i + nums[i]) % len(nums)
        visited = 1

        while slow != fast and flag and visited < len(nums):
            nextslow = (slow + nums[slow]) % len(nums)
            if direction * nums[slow] < 0:
                flag = False
                break
            slow = nextslow
            nextfast = (fast + nums[fast]) % len(nums)
            if direction * nums[fast] < 0:
                flag = False
                break
            fast = nextfast
            nextfast = (fast + nums[fast]) % len(nums)
            if direction * nums[fast] < 0:
                flag = False
                break
            fast = nextfast
            visited += 1

        # fast != (fast + nums[fast]) % len(nums) checks for 1 element loop
        # flag checks if direction's been changed
        if slow == fast and flag and fast != (fast + nums[fast]) % len(nums):
            return True
        else:
            j = i
            while j != fast and visited > 0:
                nums[j] = 0
                j = (j + nums[j]) % len(nums)
                visited -= 1
            nums[j] = 0

    return False