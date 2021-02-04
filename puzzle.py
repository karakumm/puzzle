'''
Playing board for logic puzzle
'''
def check_column(board: list, column: int) -> bool:
    '''
    Checks if the column is valid. Returns True if yes, and False if not.
    >>> check_column([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
], 4)
    False
    '''
    numbers = []
    for i in range(len(board)):
        if board[i][column] != '*' and board[i][column] != ' ':
            if board[i][column] in numbers:
                return False
            numbers.append(board[i][column])

    return True


def check_row(board: list, row: int) -> bool:
    '''
    Checks if the row is valid. Returns True if yes, and False if not.
    >>> check_row([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
], 2)
    True
    '''
    numbers = []

    for i in range(len(board)):
        if board[row][i] != '*' and board[row][i] != ' ':
            if board[row][i] in numbers:
                return False
            numbers.append(board[row][i])

    return True

def check_colors(board: list) -> bool:
    '''
    Checks if the block of each color is valid. Returns True if yes, and False if not.
    >>> check_colors([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
])
    True
    '''
    new_board = []
    for row in board:
        row = list(row)
        new_board.append(row)

    numbers = []

    color_1 = []
    for i in range(4, 9):
        color_1.append(new_board[i][0])
    for j in range(1, 5):
        color_1.append(new_board[8][j])
    numbers.append(color_1)

    color_2 = []
    for i in range(3, 8):
        color_2.append(new_board[i][1])
    for j in range(2, 6):
        color_2.append(new_board[7][j])
    numbers.append(color_2)

    color_3 = []
    for i in range(2, 7):
        color_3.append(new_board[i][2])
    for j in range(3, 7):
        color_3.append(new_board[6][j])
    numbers.append(color_3)

    color_4 = []
    for i in range(1, 6):
        color_4.append(new_board[i][3])
    for j in range(4, 8):
        color_4.append(new_board[5][j])
    numbers.append(color_4)

    color_5 = []
    for i in range(5):
        color_5.append(new_board[i][4])
    for j in range(5, 9):
        color_5.append(new_board[4][j])
    numbers.append(color_5)

    for lst in numbers:
        while ' ' in lst:
            lst.remove(' ')
        if len(set(lst)) != len(lst):
            return False
    return True

   
def validate_board(board: list) -> bool:
    '''
    Checks if the playing board is consistent with the rules.
    Returns True if yes, and False if not
    >>> validate_board([\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"\
])
    False
    '''
    for i in range(len(board)):
        if not check_column(board, i) or not check_row(board, i) or not check_colors(board):
            return False

    return True
