'''Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
    
        vow = set(['a','e','i','o','u'])

        count = 0
        ans = 0
        i=0
        
        for i in range(k):
            if s[i] in vow:
                count += 1

        if count > ans :
            ans = count

        if ans == k :
            return k

        i += 1
        

        while i < len(s): 

            if s[i - k] in vow :
                count -= 1

            if s[i] in vow:
                count += 1

            if count > ans:
                ans = count

            if ans == k:
                return k

            i += 1

        return ans
