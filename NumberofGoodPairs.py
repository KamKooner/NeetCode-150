class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = 0
        num_count = {}
        for num in nums :
            if num in num_count :
                pair += num_count[num]
                num_count[num] += 1
            else :
                num_count[num] = 1
        return pair

            
