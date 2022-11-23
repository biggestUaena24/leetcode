class Solution:
    def checkRow(self, row: List[str]) -> bool:
        res = []
        for num in row:
            if num != ".":
                if num not in res:
                    res.append(num)
                else:
                    return False
        return True

    def checkColumns(self, board: List[List[str]], index: int) -> bool:
        res = []
        for i in range(len(board)):
            if board[i][index] != ".":
                if board[i][index] not in res:
                    res.append(board[i][index])
                else:
                    return False
        return True

    def checkBox(self, board:List[List[str]], index:int) -> bool:
        res = []
        if index == 0:
            row = 0
            col = 0
        elif index == 1:
            row = 3
            col = 0
        elif index == 2:
            row = 6
            col = 0
        elif index == 3:
            row = 0
            col = 3
        elif index == 4:
            row = 3
            col = 3
        elif index == 5:
            row = 6
            col = 3
        elif index == 6:
            row = 0
            col = 6
        elif index == 7:
            row = 3
            col = 6
        elif index == 8:
            row = 6
            col = 6
        
        
        for i in range(3):
            if board[row + i][col] != ".":
                if board[row + i][col] not in res:
                    res.append(board[row + i][col])
                else:
                    return False

            if board[row + i][col + 1] != ".":
                if board[row + i][col + 1] not in res:
                    res.append(board[row + i][col + 1])
                else:
                    return False

            if board[row + i][col + 2] != ".":
                if board[row + i][col + 2] not in res:
                    res.append(board[row + i][col + 2])
                else:
                    return False
                    
        return True 

        

        
        return

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if self.checkRow(board[i]) == False:
                return False
            if self.checkColumns(board, i) == False:
                return False
            if self.checkBox(board, i) == False:
                return False
        
        return True