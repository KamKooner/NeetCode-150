class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #start your search between index 0 and the max value less than target
        i, j = 0, len(numbers)-1
        for index in range(len(numbers)):
            total = numbers[i] + numbers[j]
            if total < target:
                i+=1
            elif total > target:
                j-=1
            else:
                return [i+1, j+1]
