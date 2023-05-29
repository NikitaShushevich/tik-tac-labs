import pytest
from tic_tac_toe import check_input, check_win

def test_check_input_valid_coordinate():
    b = [["", " ", " ", " "], ["", " ", " ", " "], ["", " ", " ", " "]]
    count = 1
    coordinate = ["1", "1"]
    assert check_input(coordinate, b, count) == True

def test_check_input_invalid_coordinate():
    b = [["", " ", " ", " "], ["", " ", " ", " "], ["", " ", " ", " "]]
    count = 1
    coordinate = ["0", "4"]
    assert check_input(coordinate, b, count) == False

def test_check_input_occupied_cell():
    b = [["", " ", " ", " "], ["", " ", " ", " "], ["", " ", " ", " "]]
    count = 1
    b[1][1] = "X"
    coordinate = ["1", "1"]
    assert check_input(coordinate, b, count) == False

def test_check_win_row_winner():
    b = [["", " ", " ", " "], ["", "X", "X", "X"], ["", " ", " ", " "], ["", " ", " ", " "]]
    assert check_win(b) == "Кінець"

def test_check_win_column_winner():
    b = [["", " ", " ", " "], ["", "X", " ", " "], ["", "X", " ", " "], ["", "X", " ", " "]]
    assert check_win(b) == "Кінець"

def test_check_win_diagonal_winner():
    b = [["", " ", " ", " "], ["", "X", " ", " "], ["", " ", "X", " "], ["", " ", " ", "X"]]
    assert check_win(b) == "Кінець"

def test_check_win_draw():
    b = [["", "X", "O", "X"], ["", "O", "X", "O"], ["", "O", "X", "O"], ["", "X", "O", "X"]]
    assert check_win(b) == "Нічия"
