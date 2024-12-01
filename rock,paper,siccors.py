import random

def play_game():
    # List of possible moves
    moves = ["rock", "paper", "scissors"]
    
    # Get player's move
    player_move = input("Enter your move (rock, paper, scissors): ").lower()
    while player_move not in moves:
        player_move = input("Invalid move. Please enter rock, paper, or scissors: ").lower()
    
    # Get computer's move
    computer_move = random.choice(moves)
    print(f"Computer chose: {computer_move}")
    
    # Determine the winner
    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        print("You win!")
    else:
        print("You lose!")
    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()
