class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0 
        i,j = 0, len(height)-1

        while i<j:
            a = min(height[i],height[j]) * (j-i)
            if a > maxArea:
                maxArea = a
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return maxArea
