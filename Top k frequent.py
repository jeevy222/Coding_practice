'''Problem Statement #
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.'''


def find_k_frequent_numbers(nums, k):
    hash = {}
    temp = []
    result = [0] * k

    for i in nums:
        if i not in hash:
            hash[i] = 1
        hash[i] += 1

    for key in hash:
        pair = [key, hash[key]]
        temp.append(pair)

    temp.sort(key=lambda x: -x[1])

    for i in range(k):
        result[i] = temp[i][0]
    # TODO: Write your code

    return result


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

'''from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cntr =  Counter(nums)   
        s = sorted(cntr, key = lambda x:(-cntr[x]))
        return s[:k]
'''

