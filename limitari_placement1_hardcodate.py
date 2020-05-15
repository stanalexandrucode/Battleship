def placement1():
    shipsx1 = 3
    shipsx2 = 2
    print_board(placement1_list)
    while shipsx1 > 0:
        ships = shipsx1+shipsx2
        print("You have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(input("Choose a position to place your ship: ").lower())
        if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"]:
            row = ord(place[0])-97
            col = int(place[1])-1
            #DE AICI INCEPE HARDCODAREA
            if row == 4:
                if placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif col == 4:
                if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif row == 0:
                if placement1_list[row+1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif col == 0:
                if placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col] == 0:
                    placement1_list[row][col] = "X"
                    print_board(placement1_list)
                    shipsx1 -= 1
                else:
                    print("Ships are too close")
                    continue
            elif placement1_list[row+1][col] == placement1_list[row-1][col] == placement1_list[row][col+1] == placement1_list[row][col-1] == placement1_list[row][col] == 0:
                placement1_list[row][col] = "X"
                print_board(placement1_list)
                shipsx1 -= 1
            else:
                print("Ships are too close")
                continue
         #PANA AICI
        else:
            print("Invalid input!")
            continue
