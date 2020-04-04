'''Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]'''

from heapq import *


def find_closest_elements(arr, K, X):
    result = []
    minheap = []
    index = binary_search(arr, X)
    low, high = max(0, index - K), min(len(arr) - 1, index + K)
    for i in range(low, high + 1):
        heappush(minheap, (abs(arr[i] - X), arr[i]))
    while (K > 0):
        result.append(heappop(minheap)[1])
        K = K - 1
    result.sort()
    return result


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    if target < arr[0]:
        return start

    if target > arr[end]:
        return end
    while (end >= start):
        mid = int(start + (end - start) // 2)
        if (arr[mid] > target):
            end = mid - 1
        elif (arr[mid] < target):
            start = mid + 1
        else:
            return mid
    if (abs(arr[start] - target) < abs(target - arr[end])):
        return start
    return end


# TODO: Write your code here


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
'''Time complexity #
The time complexity of the above algorithm is O(logN + K*logK)O(logN+K∗logK). We need O(logN)O(logN) for Binary Search and O(K*logK)O(K∗logK) to insert the numbers in the Min Heap, as well as to sort the output array.

Space complexity #
The space complexity will be O(K)O(K), as we need to put a maximum of 2K numbers in the heap.'''


'''from collections import deque


def find_closest_elements(arr, K, X):
  result = deque()
  index = binary_search(arr, X)
  leftPointer, rightPointer = index, index + 1
  n = len(arr)
  for i in range(K):
    if leftPointer >= 0 and rightPointer < n:
      diff1 = abs(X - arr[leftPointer])
      diff2 = abs(X - arr[rightPointer])
      if diff1 <= diff2:
        result.appendleft(arr[leftPointer])
        leftPointer -= 1
      else:
        result.append(arr[rightPointer])
        rightPointer += 1
    elif leftPointer >= 0:
      result.appendleft(arr[leftPointer])
      leftPointer -= 1
    elif rightPointer < n:
      result.append(arr[rightPointer])
      rightPointer += 1

  return result


def binary_search(arr,  target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = int(low + (high - low) / 2)
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  if low > 0:
    return low - 1
  return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
'''
'''Time complexity #
The time complexity of the above algorithm is O(logN + K)O(logN+K). We need O(logN)O(logN) for Binary Search and O(K)O(K) for finding the ‘K’ closest numbers using the two pointers.

Space complexity #
If we ignoring the space required for the output list, the algorithm runs in constant space O(1)O(1).'''