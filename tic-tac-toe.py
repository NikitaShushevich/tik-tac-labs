def print_board(b):
    print("---------")
    print("| {} {} {} |".format(b[1][1], b[1][2], b[1][3]))
    print("| {} {} {} |".format(b[2][1], b[2][2], b[2][3]))
    print("| {} {} {} |".format(b[3][1], b[3][2], b[3][3]))
    print("---------")


def check_input(coordinate, b, count):
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


def check_win(b):
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


def play_game():
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
