import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        # Get the user's choice
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        # Validate input
        if user_choice not in choices:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Generate the computer's choice
        computer_choice = random.choice(choices)
        print(f"The computer chose: {computer_choice}")
        
        # Compare the choices to determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")
        
        # Ask if the user wants to play again
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
