class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sln = []
        nums.sort()
        print(nums)
        for l,a in enumerate(nums):
            if l>0 and a == nums[l-1]:
                continue

            #set pointers
            c = l+1 
            r = len(nums)-1

            while(c<r):
                total = a + nums[c] + nums[r]
                #shifts right pointer to left
                if(total > 0):
                    r -= 1
                #shifts center pointer to right
                elif(total < 0):
                    c += 1
                else:
                    sln.append([a, nums[c], nums[r]])   
                    c+=1
                    while(c < r and nums[c] == nums[c-1]):
                        c+=1
        return sln
            
