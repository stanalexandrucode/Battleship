def print_board(board):

    print('''
                1   2   3   4    5 

            A   {}   {}   {}   {}    {}

            B   {}   {}   {}   {}    {}

            C   {}   {}   {}   {}    {}

            D   {}   {}   {}   {}    {}

            E   {}   {}   {}   {}    {}



        '''.format(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[1][0], board[1][1], board[1][2],
                   board[1][3], board[1][4], board[2][0], board[2][1], board[2][2], board[2][3], board[2][4],
                   board[3][0], board[3][1], board[3][2], board[3][3], board[3][4],
                   board[4][0], board[4][1], board[4][2], board[4][3], board[4][4]))


def placement1():
    shipsx1 = 3
    shipsx2 = 2
    print_board(placement1_list)
    while shipsx1 > 0:
        ships = shipsx1+shipsx2
        print("You have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(input("Choose a position to place your ship: ").lower())
        row = ord(place[0])-97
        col = int(place[1])-1
        placement1_list[row][col] = "X"
        print_board(placement1_list)
        shipsx1 -= 1
    while shipsx2 > 0:
        ships = shipsx1+shipsx2
        print("You have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        direction = input(
            "Choose on wich direction you want to place your ship (N,S,E,W) :").lower()
        row = ord(place[0])-97
        col = int(place[1])-1
        placement1_list[row][col] = "X"
        if direction == "n":
            placement1_list[row-1][col] = "X"
        if direction == "s":
            placement1_list[row+1][col] = "X"
        if direction == "e":
            placement1_list[row][col+1] = "X"
        if direction == "w":
            placement1_list[row][col-1] = "X"
        print_board(placement1_list)
        shipsx2 -= 1


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
placement1_list = board
placement1()
