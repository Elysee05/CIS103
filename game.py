# CIS 103: Introduction to Programming
# Lab 01: "Calculator Function"
# Student: Elysee fleurant
# Date: 08/31/2024
#
import random
while True:
    print("1. play")
    print("2. Exit")
    choice = input("Enter choice: ")
    if choice == '2':
            print("exiting, thank you Good Game!")
            break
    if choice == '1':    print("welcome to the Game!")
    user_action = input("Choose your weapon (rock, paper, scissors):")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"Your weapon {user_action}, Kilroy's weapon {computer_action}.\n")
    if user_action == computer_action:
        print("{user_action} Draw!")
    elif user_action == "rock" and computer_action == "scissors":
        print("You Win!")
    elif user_action == "paper" and computer_action == "rock":
        print("You Win!")
    elif user_action == "scissors" and computer_action == "paper":
        print("You Win!")
    else:
        print("K.O. You Lose")
def main():
    if __name__ == "__main__":
        main()

