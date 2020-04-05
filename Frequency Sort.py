'''Problem Statement #
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.'''


def sort_character_by_frequency(str):
    # TODO: Write your code here
    hash = {}
    temp = []
    result = []
    for i in range(len(str)):
        if str[i] not in hash:
            hash[str[i]] = 0
        hash[str[i]] += 1

    for key in hash:
        pair = [key, hash[key]]
        temp.append(pair)

    temp.sort(key=lambda x: -x[1])
    print(temp)

    for i in range(len(temp)):
        while (temp[i][1] > 0):
            result.append(temp[i][0])
            temp[i][1] -= 1
    return ''.join(result)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
