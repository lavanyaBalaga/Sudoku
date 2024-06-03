import numpy
sudoku=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
def is_valid(num,row,col):
    for i in range(len(sudoku)):
        if sudoku[row][i]==num:return False#checking whether the number is there in the same row
    for i in range(len(sudoku)):
        if sudoku[i][col]==num:return False#checking whether the number is there in the same column
    box_r=(row//3)*3
    box_c=(col//3)*3
    for i in range(box_r,box_r+3):#[getting the box values separate]
        for j in range(box_c,box_c+3):
            if sudoku[i][j]==num:#checking whether the number is there in the same box
              return False
    return True
def solve_sudoku(sudoku): 
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j]==0:
                for num in range(1,10):
                    if is_valid(num,i,j):
                        sudoku[i][j]=num
                        if solve_sudoku(sudoku): 
                            return True  
                        sudoku[i][j] = 0 
                return 
                
    print(numpy.matrix(sudoku))   
solve_sudoku(sudoku)     


######################################################################################################################
output:
[[3 1 6 5 7 8 4 9 2]
 [5 2 9 1 3 4 7 6 8]
 [4 8 7 6 2 9 5 3 1]
 [2 6 3 4 1 5 9 8 7]
 [9 7 4 8 6 3 1 2 5]
 [8 5 1 7 9 2 6 4 3]
 [1 3 8 9 4 7 2 5 6]
 [6 9 2 3 5 1 8 7 4]
 [7 4 5 2 8 6 3 1 9]]
