import random


def get_amount_pencil():
    print("How many pencils would you like to use:")
    while True:
        pencils = input()
        if not pencils.isnumeric():
            print("The number of pencils should be numeric")
        elif int(pencils) <= 0:
            print("The number of pencils should be positive")
        else:
            pencils = int(pencils)
            return pencils


def get_first_player(players):
    print("Who will be the first (John, Jack):")
    while True:
        first_player = input()
        if first_player not in players:
            print(f"Choose between '{players[0]}' and '{players[1]}'")
        else:
            return first_player


def get_taken_pencil(pencils_remain, is_jack_player_turn):
    while True:
        if is_jack_player_turn:
            pencils = pencils_remain % 4
            if pencils == 0:
                pencils = 4
            pencils -= 1

            if pencils == 0:
                max_value = 3 if pencils_remain >= 4 else pencils_remain
                pencils = random.randint(1, max_value)

            print(pencils)
            return pencils
        else:
            pencils = input()
            if not pencils.isnumeric():
                print("Possible values: '1', '2' or '3'")
            else:
                pencils = int(pencils)
                if pencils <= 0 or pencils > 3:
                    print("Possible values: '1', '2' or '3'")
                elif pencils > pencils_remain:
                    print("Too many pencils were taken")
                else:
                    return pencils


def next_player(players, player_turn):
    position = players.index(player_turn) + 1
    position = position % len(players)
    return players[position]


def start_game(pencils, players, player_turn):
    while pencils > 0:
        is_jack_player_turn = player_turn == players[1]
        print("|" * pencils)
        print(f"{player_turn}'s turn!")
        pencils_taken = get_taken_pencil(pencils, is_jack_player_turn)
        pencils -= pencils_taken
        player_turn = next_player(players, player_turn)

    print(f"{player_turn} won!")


def main():
    players = ["John", "Jack"]
    pencils = get_amount_pencil()
    first_player = get_first_player(players)
    start_game(pencils, players, first_player)


if __name__ == "__main__":
    main()
