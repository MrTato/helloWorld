import random

will_play_again = True

while will_play_again:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()


    def check_for_win(player_choice, computer_choice):
        if player_choice == computer_choice:
            return 0
        if player_choice == "rock" and computer_choice == "paper"\
                or player_choice == "paper" and computer_choice == "scissors"\
                or player_choice == "scissors" and computer_choice == "rock":
            return -1
        return 1


    print("computer: ", computer)
    print("player: ", player)
    win_value = check_for_win(player, computer)
    if win_value == -1:
        print("You lose!")
    elif win_value == 0:
        print("Tie")
    else:
        print("You win!")
    play_again = input("Play again? (yes/no): ").lower()

    will_play_again = play_again == "yes"