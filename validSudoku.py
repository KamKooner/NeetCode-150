class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  
            
        #check rows
        for i in range(len(board)):
            rowCheck = {}  
            for j in range(len(board[i])):
                if(board[i][j].isdigit() and board[i][j] not in rowCheck):
                    rowCheck[board[i][j]] = 1
                elif (not board[i][j].isdigit()):
                    continue
                else:
                    
                    return False
        #check columns
        for i in range(len(board)):
            colCheck = {}
            for j in range(len(board[i])):
                if(board[j][i].isdigit() and board[j][i] not in colCheck):
                    colCheck[board[j][i]] = 1
                elif (not board[j][i].isdigit()):
                    continue
                else:
                    return False
                
        squares = collections.defaultdict(set)
        #check 3x3 sub-grids
        for r in range(9):
            for c in range(9):
                if(not board[r][c].isdigit()):
                    continue
                if(board[r][c] in squares[(r//3, c//3)]):
                    return False
                squares[(r//3, c//3)].add(board[r][c])
        return True
