

#Is the entire sudoku solved correctly already?
def isSolvedBoard(board):
  for row in range(len(board)):
    for col in range(len(board[0])):
        if(board[row][col] < 1 or board[row][col] > 9): #invalid number exists
          return False
        if(not validMove(board, row, col, board[row][col])): #conflict exists
          return False
  return True

#Are two coordinates in the same square?
def sameSquare(row1, col1, row2, col2):
    return row1 // 3 == row2 // 3 and col1 // 3 == col2 // 3


#Would placing num in the rowth row and colth column conflict with any numbers in the current board?
def validMove(board, row, col, num):
  for newRow in range(len(board)):
      for newCol in range(len(board[0])):
        if(not(newRow == row and newCol == col) and board[newRow][newCol] == num): #find other occurences of num
          if(newRow == row or newCol == col or sameSquare(newRow, newCol, row, col)): #same row, column, or square
            return False
  return True

def sudokuSolver(board):
  if(isSolvedBoard(board)): #board is solved already
    return board
  else:
    for row in range(len(board)):
      for col in range(len(board[0])):
          if(board[row][col] > 9 or board[row][col] < 1):
            for num in (1,2,3,4,5,6,7,8,9):
               if(validMove(board, row, col, num)):    #check if any of integers 1-9 work in (row, col)
                 board[row][col] = num                 #if yes, set it
                 newBoard = sudokuSolver(board)  #try the same thing on the changed board
                 if(newBoard != None): #the next check didn't fail
                   return newBoard #Finished
                 else:
                  board[row][col] = 0 #must reset values if failed
    return None



#Test cases to play around with
solved = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
     [8, 4, 2, 9, 7, 3, 5, 6, 1],
     [9, 6, 1, 2, 8, 5, 3, 7, 4],
     [2, 8, 6, 3, 4, 9, 1, 5, 7],
     [4, 1, 3, 8, 5, 7, 9, 2, 6],
     [5, 7, 9, 1, 2, 6, 4, 3, 8],
     [1, 5, 7, 4, 9, 2, 6, 8, 3],
     [6, 9, 4, 7, 3, 8, 2, 1, 5],
     [3, 2, 8, 5, 6, 1, 7, 4, 9]]

easy1 = [[0, 2, 0, 4, 5, 6, 7, 8, 9],
     [4, 5, 7, 0, 8, 0, 2, 3, 6],
     [6, 8, 9, 2, 3, 7, 0, 4, 0],
     [0, 0, 5, 3, 6, 2, 9, 7, 4],
     [2, 7, 4, 0, 9, 0, 6, 5, 3],
     [3, 9, 6, 5, 7, 4, 8, 0, 0],
     [0, 4, 0, 6, 1, 8, 3, 9, 7],
     [7, 6, 1, 0, 4, 0, 5, 2, 8],
     [9, 3, 8, 7, 2, 5, 0, 6, 0]]

easy2 = [[0, 2, 0, 5, 0, 1, 4, 0, 3],
     [1, 0, 3, 0, 6, 4, 0, 0, 7],
     [0, 0, 4, 3, 0, 0, 0, 5, 1],
     [4, 0, 0, 0, 0, 0, 5, 1, 6],
     [0, 6, 0, 0, 1, 3, 0, 4, 0],
     [7, 1, 0, 0, 4, 5, 3, 0, 2],
     [0, 9, 2, 1, 0, 6, 0, 0, 0],
     [8, 7, 6, 4, 3, 0, 1, 2, 0],
     [0, 0, 0, 0, 7, 0, 6, 0, 0]]


medium = [[1, 4, 0, 5, 0, 6, 3, 0, 0],
     [3, 0, 0, 0, 0, 0, 0, 8, 0],
     [9, 8, 2, 4, 1, 3, 0, 0, 0],
     [0, 0, 0, 8, 0, 0, 0, 0, 9],
     [0, 7, 6, 3, 0, 0, 1, 2, 0],
     [8, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 2, 3, 7, 8, 1, 5],
     [0, 5, 0, 0, 0, 0, 0, 0, 6],
     [0, 0, 8, 6, 0, 5, 0, 3, 4]]


hard = [[0, 0, 0, 2, 0, 0, 0, 6, 3],
     [3, 0, 0, 0, 0, 5, 4, 0, 1],
     [0, 0, 1, 0, 0, 3, 9, 8, 0],
     [0, 0, 0, 0, 0, 0, 0, 9, 0],
     [0, 0, 0, 5, 3, 8, 0, 0, 0],
     [0, 3, 0, 0, 0, 0, 0, 0, 0],
     [0, 2, 6, 3, 0, 0, 5, 0, 0],
     [5, 0, 3, 7, 0, 0, 0, 0, 8],
     [4, 7, 0, 0, 0, 1, 0, 0, 0]]

####change the puzzle####
puzzle = easy1
#########################
for row in range(len(puzzle)):
    for col in range(len(puzzle[0])):
        print(sudokuSolver(puzzle)[row][col], end='')
        print(' ', end='')
    print('\n', end='')
