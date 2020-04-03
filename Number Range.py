'''Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].'''

'''Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]'''

def find_range(arr, key):
  result = [- 1, -1]
  result[0] = Binary_search(arr, key, False)
  if result[0] != -1:
    result[1] = Binary_search(arr, key , True)


  return result

def Binary_search(arr, key,x ):
  start = 0
  end = len(arr)-1
  keyindex = -1
  while(end>= start):
    mid = (start+end)//2
    if ( key > arr[mid]):
      start = mid + 1
    elif(key<arr[mid]):
      end = mid - 1
    else:
      keyindex = mid
      if x:
        start = mid + 1
      else:
        end = mid -1
  return  keyindex

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()


'''The problem follows the Binary Search pattern. Since Binary Search helps us find a number in a sorted array efficiently, we can use a modified version of the Binary Search to find the first and the last position of a number.

We can use a similar approach as discussed in Order-agnostic Binary Search. We will try to search for the ‘key’ in the given array; if the ‘key’ is found (i.e. key == arr[middle) we have two options:

When trying to find the first position of the ‘key’, we can update end = middle - 1 to see if the key is present before middle.
When trying to find the last position of the ‘key’, we can update start = middle + 1 to see if the key is present after middle.
In both cases, we will keep track of the last position where we found the ‘key’. These positions will be the required range.'''