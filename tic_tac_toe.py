def print_board(b:str)->str:
    """
The print_board (b) function displays the current state of the game board b.
 It uses string formatting to display each board cell.
    :param b:
    :return:
    """
    print("---------")
    print(f"| {b[1][1]} {b[1][2]} {b[1][3]} |")
    print(f"| {b[2][1]} {b[2][2]} {b[2][3]} |")
    print(f"| {b[3][1]} {b[3][2]} {b[3][3]} |")
    print("---------")


def check_input(coordinate:int, b:str, count:int)->bool:
    """
The check_input function (coordinate, b, count) checks the correctness of the entered
coordinates coordinate and whether this cell is free to move.
    :param coordinate:
    :param b:
    :param count:
    :return:
    """
    if coordinate[0].isnumeric() != True or coordinate[1].isnumeric() != True:
        print('Можна вводити тільки цифри!')
        return False
    elif int(coordinate[0]) > 3 or int(coordinate[0]) == 0 or int(coordinate[1]) > 3 or int(coordinate[1]) == 0:
        print('Координати повинні бути від 1 до 3!')
        return False
    elif b[int(coordinate[0])][int(coordinate[1])] == "X" or b[int(coordinate[0])][int(coordinate[1])] == "O":
        print("Ця клітинка зайнята! Вибери іншу!")
        return False
    else:
        if count % 2 != 0:
            b[int(coordinate[0])][int(coordinate[1])] = "X"
            return True
        else:
            b[int(coordinate[0])][int(coordinate[1])] = "O"
            return True


def check_win(b:str)->str:
    """
The check_win (b) function checks whether there is a winning state on the game board b.
It checks rows, columns, and diagonals to make sure all cells have the same value (either "X" or "O").
    :param b:
    :return:
    """
    columb_row = [any([b[1][n] == b[2][n] == b[3][n] == "X" or b[1][n] == b[2][n] == b[3][n] == "O" or b[n][1] == b[n][
        2] == b[n][3] == "X" or b[1][n] == b[2][n] == b[3][n] == "O"]) for n in range(1, 4)]
    cross = [b[1][1] == b[2][2] == b[3][3] == 'X' or b[1][1] == b[2][2] == b[3][3] == 'O' or b[1][3] == b[2][2] == b[3][
        1] == "X" or b[1][3] == b[2][2] == b[3][1] == "O"]
    if any(columb_row):
        return "Кінець"
    elif any(cross):
        return "Кінець"
    elif all([all([i != " " for i in row]) for row in b]):
        return "Нічия"
    else:
        return "продовження"


def play_game()->str:
    """
Function play_game () performs a game of cross-tic-tac-toe. It initializes an empty game board b and sets the move counter to 1.
It displays the current state of the board until check_win (b) returns "finish" or "draw."
    :return:
    """
    b = [[], ["", " ", " ", " "], ["", " ", " ", " "], ["", " ", " ", " "]]
    count = 1
    start = "продовження"
    print_board(b)

    while start == "продовження":
        coordinate = input('Введіть координати (наприклад 1 1): ').split()
        if check_input(coordinate, b, count):
            count += 1
            print_board(b)
            start = check_win(b)

    if start == "finish":
        print(f"{b[int(coordinate[0])][int(coordinate[1])]} виграв")
    else:
        print('Draw')


if __name__ == "__main__":
    play_game()
