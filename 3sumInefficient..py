lass Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sln = []
        if len(nums) == 0:
            return []
            
        #moves left pointer
        for i in range(len(nums)):
            k = i+1 
            j=len(nums) -1
            #moves right pointer
            while j>k:
                #moves inner pointer
                while k < j:
                    print(i,j,k)
                    if i!=k and i!=j and j!=k and nums[i] + nums[j] + nums[k] == 0:
                        candidate = sorted([nums[i], nums[j], nums[k]])
                        if candidate not in sln:
                            sln.append(candidate)
                    k+=1
                j-=1
                k=i+1
            
        return sln
