class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        i =0
        j = len(height)-1
        while(i<j):
            result = max(result,min(height[i],height[j])*(j-i))
            if(height[j]>height[i]):
                i+=1
            else:
                j-=1
        return(result)