#import tictactoe


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
x_o_sum = (x_count + o_count)
if x_count > o_count and x_o_sum < 9:
    print("O is next,board count: %d " % x_o_sum )
elif o_count > x_count and x_o_sum < 9:
    print("X is next")
elif x_o_sum == 9:
    print("Board full.")


def count_board(board):
    x_count = 0
    o_count = 0
    empty_count = 0
    board_counts = []
    for row in board:
        for element in row:
            if element == X:
                x_count += 1
            elif element == O:
                o_count += 1
            elif element == EMPTY:
                empty_count += 1
    x_o_sum = (x_count + o_count)
    board_counts.append(x_count)
    board_counts.append(o_count)
    board_counts.append(empty_count)
    board_counts.append(x_o_sum)
    
    return board_counts
print(count_board(board4))
count_board(board2)




