EMPTY = "EMPTY"
X = "X"
O = "O"
board1 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board2 = [[EMPTY, "X", EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board3 = [[EMPTY, "X", "O"],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def count_board(board):
    x_count = 0
    o_count = 0
    empty_count = 0
    for i in board:
        print(i[0])
        if i[0] == X:
            x_count += 1
            
        elif i[0] == O:
            o_count += 1
        elif i[0] == 'EMPTY':
            empty_count += 1
        if i[1] == X:
            x_count += 1
            
        elif i[1] == O:
            o_count += 1
        elif i[1] == 'EMPTY':
            empty_count += 1
        if i[2] == X:
            x_count += 1
            
        elif i[2] == O:
            o_count += 1
        elif i[2] == 'EMPTY':
            empty_count += 1
    print(x_count,o_count,empty_count)
count_board(board2)