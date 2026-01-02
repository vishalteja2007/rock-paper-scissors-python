
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    ties = 0

    print("Welcome to Rock Paper Scissors!")
    print("--------------------------------")
    print("Type 'rock', 'paper', 'scissors', or 'quit' to exit.\n")

    while True:
        player = input("Your choice: ").lower().strip()

        if player == "quit":
            break

        if player not in choices:
            print("Invalid choice! Try again.\n")
            continue

        computer = random.choice(choices)

        print(f"\nYou chose: {player.title()}")
        print(f"Computer chose: {computer.title()}")

        if player == computer:
            print("It's a tie!")
            ties += 1

        elif (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
        ):
            print("You win this round!")
            player_score += 1

        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Scores → You: {player_score} | Computer: {computer_score} | Ties: {ties}\n")

    print("\nFinal Scores:")
    print(f"You: {player_score} | Computer: {computer_score} | Ties: {ties}")

    if player_score > computer_score:
        print(" Congratulations! You won the game!")
    elif computer_score > player_score:
        print(" Computer wins overall!")
    else:
        print(" Game ended in a tie!")

if __name__ == "__main__":
    play_game()