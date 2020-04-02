'''Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given ‘key’.'''

def search_next_letter(arr,key):
    start = 0
    end = len(arr)-1
    if (key>arr[end] or key<arr[start]):
        return arr[0]

    while(start<=end):
        mid = start + (end-start)//2
        if(key>arr[mid]):
            start = mid + 1
        elif(key<arr[mid]):
            end = mid - 1
    return arr[start%len(arr)]

def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()