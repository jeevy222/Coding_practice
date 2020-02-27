import collections


class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:
        # count = 0

        # for i in J:
        #   for k in S:
        #      if(ord(i)==ord(k)):
        #         count+=1
        # return count
        Jset = set(J)
        return sum(s in Jset for s in S)
