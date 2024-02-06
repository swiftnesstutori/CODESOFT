# rock, paper, scissors game
import random
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return "It's a tie!",0,0
    elif (user_action == "rock" and computer_action == "scissors") or  (user_action == "paper" and computer_action == "rock") or (user_action == "scissors" and computer_action == "paper"):
        return "You Win!",1,0
    else:
        return "You Lose!",0,1
def main():
    user_score = 0
    computer_score = 0
    rounds = 0
    while True:
        user_action = input("Enter a choice (rock, paper, scissors) or 'exit' to end : ")
        if user_action == 'exit':
            break
        if user_action not in ["rock","paper","scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors")
            continue
        computer_action = random.choice(["rock", "paper", "scissors"])
        print(f"\nYour choice {user_action}, computer choice {computer_action}.")
        result, user_round_score, computer_round_score = determine_winner(user_action, computer_action)
        print(result)
        user_score += user_round_score
        computer_score += computer_round_score
        rounds += 1
    print(f"\nTotal rounds played : {rounds}")
    print(f"Your score : {user_score}, computer's score : {computer_score}")
if __name__ == "__main__":
    main()