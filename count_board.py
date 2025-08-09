EMPTY = "EMPTY"
X = "X"
O = "O"
board1 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board2 = [[EMPTY, "X", "O",
           EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board3 = [[EMPTY, "X", "O"],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
board4 = [["X", "X", "O"],
            ["O", "X", "O"],
            ["X", "X", "O"]]
x_count = 0
o_count = 0
empty_count = 0
for row in board4:
    for element in row:
        print(element)
        if element == X:
            x_count += 1
        elif element == O:
            o_count += 1
        elif element == 'EMPTY':
            empty_count += 1
if x_count > o_count:
    print("O is next")
elif o_count > x_count:
    print("X is next")
elif x_count == o_count & x_count + o_count < 9:
    print("X goes next, board count is %d" % (x_count + o_count))
elif x_count + o_count == 9:
    print("Game over")


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
