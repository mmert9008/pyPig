import random


def roll():
    min_roll = 1
    max_roll = 6
    roll = random.randint(min_roll, max_roll)

    return roll


def main():
    while True:
        num_players = input("Enter the number of players (2-4): ")
        if num_players.isdigit():
            num_players = int(num_players)
            if 2 <= num_players <= 4:
                break
            else:
                print("Must be between 2 and 4 players.")
        else:
            print("Please enter a valid number of players.")

    max_score = 50
    player_scores = [0 for _ in range(num_players)]

    while max(player_scores) < max_score:
        for player_index in range(num_players):
            print(f"\nPlayer {player_index + 1}'s turn:")
            print(f"Your current score is {player_scores[player_index]}\n")
            current_score = 0

            while True:
                wanna_roll = input(
                    f"Player {player_index + 1}, would you like to roll (y)? "
                )
                if wanna_roll.lower() != "y":
                    break

                turn = roll()
                if turn == 1:
                    print("You rolled a 1 and ended your turn")
                    current_score = 0
                    break
                else:
                    current_score += turn
                    print(f"You rolled a {turn}")

                print(f"Your score is {current_score}")

            player_scores[player_index] += current_score
            print(f"\nYour total score is {player_scores[player_index]}\n\n")

    max_score = max(player_scores)
    winner_index = player_scores.index(max_score)

    print(
        f"Player {winner_index + 1} wins! Player {winner_index + 1} scored {max_score}!"
    )


if __name__ == "__main__":
    main()
