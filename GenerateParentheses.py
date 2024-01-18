class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        final = []
        word = ""
        #Terminate when we have n open, and n closed brackets
        #add opening when openingCount < n 
        #can only add a closing if openingCount > closingCount
        
        def myRecursion(oC, cC):
            if (oC == n and cC == n):
                final.append("".join(temp))
                return
            if (oC < n):
                temp.append("(")
                myRecursion(oC + 1, cC)
                temp.pop()
            if (cC < oC):
                temp.append(")")
                myRecursion(oC, cC + 1)
                temp.pop()
        myRecursion(0,0)
        return final

