'''
Table:
    (1,1) | (1,2) | (1,3)
    (2,1) | (2,2) | (2,3)
    (3,1) | (3,2) | (3,3)
'''
def check_xo(address, xxx, ooo):
    if address in xxx:
        state_address = "X"
    elif address in ooo:
        state_address = "O"
    else:
        state_address = " "
    return state_address

def determine(xxx):
    line_row_1 = 0
    line_row_2 = 0
    line_row_3 = 0
    line_col_1 = 0
    line_col_2 = 0
    line_col_3 = 0
    bingo = False
    for x in xxx:
        # print(x[0])
        if x[0] == 1:
            line_row_1 += 1
        if x[0] == 2:
            line_row_2 += 1
        if x[0] == 3:
            line_row_3 += 1
        if x[1] == 1:
            line_col_1 += 1
        if x[1] == 2:
            line_col_2 += 1
        if x[1] == 3:
            line_col_3 += 1

    if line_row_1 == 3:
        bingo = True
    elif line_row_2 == 3:
        bingo = True
    elif line_row_3 == 3:
        bingo = True
    elif line_col_1 == 3:
        bingo = True
    elif line_col_2 == 3:
        bingo = True
    elif line_col_3 == 3:
        bingo = True
    elif {(1,1), (2,2), (3,3)}.issubset(xxx):
        bingo = True
    elif {(1,3), (2,2), (3,1)}.issubset(xxx):
        bingo = True

    # print(bingo)
    return bingo


def print_tic(
    xxx,
    ooo,
    ):

    state_11 = check_xo((1,1), xxx, ooo)
    state_12 = check_xo((1,2), xxx, ooo)
    state_13 = check_xo((1,3), xxx, ooo)
    state_21 = check_xo((2,1), xxx, ooo)
    state_22 = check_xo((2,2), xxx, ooo)
    state_23 = check_xo((2,3), xxx, ooo)
    state_31 = check_xo((3,1), xxx, ooo)
    state_32 = check_xo((3,2), xxx, ooo)
    state_33 = check_xo((3,3), xxx, ooo)

    print(f" {state_11} | {state_12} | {state_13} ")
    print("-----------")
    print(f" {state_21} | {state_22} | {state_23} ")
    print("-----------")
    print(f" {state_31} | {state_32} | {state_33} ")


def main():
    print("  col | 1 | 2 | 3 ")
    print("row 1 |   |   |   ")
    print("------------------")
    print("row 2 |   |   |   ")
    print("------------------")
    print("row 3 |   |   |   ")
    # print("------------------")

    xxx = []
    ooo = []
    x_user_move = True

    end_of_game = False
    while end_of_game == False:
        print("================================================")
        # print(x_user_move)
        valid_input = False
        while valid_input == False:
            if x_user_move == True:
                print("Now it's the X user move")
            else:
                print("Now it's the O user move")
            move_row = int(input("input your move row {1,2,3}: "))
            move_col = int(input("input your move column {1,2,3}: "))

            # check valid input
            if move_row not in [1,2,3] or move_col not in [1,2,3]:
                print("ERROR: unvalid input, not in {1,2,3}")
            elif (move_row, move_col) in xxx:
                print("ERROR: unvalid, it's signed by X")
            elif (move_row, move_col) in ooo:
                print("ERROR: unvalid, it's signed by O")
            else:
                # correct input
                if x_user_move:
                    xxx.append((move_row, move_col))
                else:
                    ooo.append((move_row, move_col))
                valid_input = True
        # print(f"xxx = {xxx}")
        # print(f"ooo = {ooo}")

        # print table
        print_tic(
            xxx,
            ooo,
        )

        # determine who win
        win_x = determine(xxx)
        win_o = determine(ooo)
        if win_x == True:
            print("X user win!")
            end_of_game = True
        elif win_o == True:
            print("O user win!")
            end_of_game = True

        x_user_move = not(x_user_move)



if __name__ == "__main__":
    main()
    # xxx = [(1,1), (2,2), (3,3)]
    # ooo = [(1,1), (1,2), (1,3)]
    # determine(xxx)
    # determine(ooo)

