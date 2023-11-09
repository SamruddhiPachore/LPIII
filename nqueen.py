def nQueens(n) -> list[list[str]]:
    col = set()
    posDiag = set()
    negDiag = set()
    
    result = []

    board = [["."]*n for _ in range(n)]


    print(board)
    def backtrack(r,count):
        if r==n:
            copy_board = ["".join(row) for row in board]
            result.append(copy_board)
            return
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue
            board[r][c] = "Q"

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)

            backtrack(r+1,count)

        
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."

    backtrack(0,0)
    return result,len(result)

if __name__=="__main__":
    print(nQueens(4))    