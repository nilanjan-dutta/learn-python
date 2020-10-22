from os import system, name


board_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def welcome_players():
    print("Welcome to the Tic Tac Toe Game for 2 players ! \n")
    print("Player One plays with: X")
    print("Player Two plays with: O \n")
    is_game_over = start_game()
    if is_game_over:
        repeat_confirmation = input(
            "To continue press 'Y'. Press any other key to exit.")
        if repeat_confirmation == "Y" or repeat_confirmation == "y":
            global board_list
            board_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            welcome_players()


def start_game():
    user_text = " "
    while user_text != "":
        user_text = input("To start playing, press Enter")
    clear_screen()
    print_board(board_list)

    def game_over():
        def check_all_equal(collection):
            for item in collection:
                if len(set(item)) == 1:
                    return item[0]
            return -1

        def match_tie():
            count = 0
            for rows in board_list:
                for item in rows:
                    if item == 'X' or item == 'O':
                        count += 1
            return count == 9

        def check_rows():
            return check_all_equal(board_list)

        def check_columns():
            columns = [[board_list[0][0], board_list[1][0], board_list[2][0]],
                       [board_list[0][1], board_list[1][1], board_list[2][1]],
                       [board_list[0][2], board_list[1][2], board_list[2][2]]]

            return check_all_equal(columns)

        def check_diagonals():
            diagnoals = [[board_list[0][0], board_list[1][1], board_list[2][2]],
                         [board_list[0][2], board_list[1][1], board_list[2][0]]]
            return check_all_equal(diagnoals)

        row_check = check_rows()
        column_check = check_columns()
        diagonal_check = check_diagonals()

        final_result_set = set([row_check, column_check, diagonal_check])

        if len(final_result_set) == 1 and final_result_set.pop() == -1 and not match_tie():
            return False
        elif match_tie():
            print("Bummer !!! The match is a tie !")
            return True
        else:
            winner = final_result_set.pop()
            print("Congratulations!!! Frst Player is the WINNER !!!!") if winner == 'X' else print(
                "Congratulations!!! Second Player is the WINNER !!!!")
            return True

    while not game_over():
        first_user_input = 0
        while first_user_input == 0 and (first_user_input not in board_list):
            first_user_input = input("1st User (X): Enter your choice: ")
        update_board_list(first_user_input, 'X')
        clear_screen()
        print_board(board_list)

        if game_over():
            break

        second_user_input = 0
        while second_user_input == 0 and (second_user_input not in board_list):
            second_user_input = input("2nd User (O): Enter your choice: ")

        update_board_list(second_user_input, 'O')
        clear_screen()
        print_board(board_list)

    return True


def update_board_list(user_choice_index: str, choice: str):
    for row in board_list:
        if user_choice_index in row:
            row[row.index(user_choice_index)] = choice


def print_board(cells: list = []):
    if len(cells) == 0:
        print("Didn't receive the board values.")
        return

    def print_rows(rows: list):
        print("-- --- --")
        print(" | ".join(rows))

    for row in board_list:
        print_rows(row)


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')


welcome_players()
