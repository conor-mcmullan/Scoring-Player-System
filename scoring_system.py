import thread

score_system = {}


def set_player_list(player_count):
    score_system.clear()
    for player in xrange(player_count):
        score_system.update({chr(ord('a')+player): 0})


def print_scoreboard():
    for key in sorted(score_system):
        if key is sorted(score_system)[-1]: v = "%s: %s"
        else: v = "%s: %s, "
        print v % (key, score_system[key]),
    println(add_line(1))


def update_player_score(player):
    if str(player).lower() in score_system.keys():
        if str(player).islower():
            score_system[str(player).lower()] += 1
        elif str(player).isupper():
            score_system[str(player).lower()] -= 1
    else: println(add_line(1)+"NON_VALID_PLAYER"+add_line(1))
    print_scoreboard()


def add_line(num):
    for n in xrange(num):
        return "\n"


def println(msg):
    print str(msg)


def start_menu_system():
    user_input = -1
    while(user_input not in [0, 1]):
        println(add_line(3)+"START MENU"+add_line(1)+"1: Start Game")
        println("0: Exit Game"+add_line(2)+"...")
        try:
            user_input = int(raw_input('choice: '))
        except ValueError:
            println(add_line(1)+"| Not a valid choice |")
        finally:
            if user_input is 0:
                exit(0)
            elif user_input is 1:
                main_menu()
            else:
                println(add_line(1) + "| Not a valid choice|")
                start_menu_system()


def main_menu():
    user_input = -1
    while (user_input not in [0, 1, 2]):
        println(add_line(2)+"MAIN MENU"+add_line(1)+"1: Enter Number Of Players")
        println("2: View Instructions")
        println("0: Exit Game" + add_line(2) + "...")
        try:
            user_input = int(raw_input('choice: '))
        except ValueError:
            println(add_line(1) + "| Not a valid choice|")
        finally:
            if user_input is 0:
                exit(0)
            elif user_input in [1, 2]:
                in_game_menu(user_input)
            else:
                println(add_line(1) + "| Not a valid choice|")


def in_game_menu(case):
    if case is 1:
        user_input = -1
        while (user_input < 1 or user_input > 26):
            println(add_line(2) + "IN GAME MENU"+add_line(1))
            try:
                user_input = int(raw_input('Enter Number Of Players: '))
                if (user_input < 1 or user_input > 26):
                    println(add_line(1)+"| Not a valid number of players |")
            except ValueError:
                println(add_line(1) + "| Not a valid number|")
            finally:
                if (user_input < 1 or user_input > 26):
                    println(add_line(1) + "| Not a valid number|")
                else:
                    set_player_list(user_input)
                    game_loop()

    elif case is 2:
        println(add_line(2)+"Altering the scores."+
                add_line(1)+"Scores a point: the letter of players name is typed in lowercase."+
                add_line(1)+"Loses a point:  the letter of players name is typed in uppercase.")
        main_menu()


def game_loop():
    user_input = "not end"
    print_scoreboard()
    while (user_input != ("END" or "end")):
        try:
            println(add_line(2)+"LOWER = ++"+add_line(1)+"UPPER = --" + add_line(1))
            user_input = str(raw_input('player: '))
        except ValueError:
            println(add_line(1) + "| Not a valid choice |")
        finally:
            if user_input == ("END" or "end"):
                start_menu_system()
            elif user_input != ("END" or "end"):
                if len(user_input) > 1:
                    solve_a_string(user_input)
                else:
                    update_player_score(user_input)


def solve_a_string(solve):
    for letter in xrange(len(solve)):
        update_player_score(solve[letter])


if __name__ == "__main__":
    thread.start_new_thread(start_menu_system())