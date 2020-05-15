def get_shot_input():
    x = 0
    while x == 0:
        shot = str(input("Choose a position to shot: ").lower())
        if shot[0] in ["a", "b", "c", "d", "e"] and shot[1] in ["1", "2", "3", "4", "5"]:
            row = row = ord(shot[0])-97
            col = int(shot[1])-1
            x = 1
            print(row, col)
        else:
            print("Invalid input. Try again.")
            continue


get_shot_input()
