'''Rotation Count
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.'''

'''Example :

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.'''


def count_rotations(arr):
    # TODO: Write your code here
    start = 0
    end = len(arr) - 1
    while (start < end):
        mid = (start + end) // 2

        if (mid < end and arr[mid] > arr[mid + 1]):
            return mid + 1
        elif (mid > start and arr[mid - 1] > arr[mid]):
            return mid

        if (arr[start] < arr[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()


'''In this problem, actually, we are asked to find the index of the minimum element. The number of times the minimum element is moved to the right will be equal to the number of rotations. An interesting fact about the minimum element is that it is the only element in the given array which is smaller than its previous element. Since the array is sorted in ascending order, all other elements are bigger than their previous element.

After calculating the middle, we can compare the number at index middle with its previous and next number. This will give us two options:

If arr[middle] > arr[middle + 1], then the element at middle + 1 is the smallest.
If arr[middle - 1] > arr[middle], then the element at middle is the smallest.'''