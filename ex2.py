import random

while True:
    user1_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    user2_action = input("Enter a choice (rock, paper, scissors): ")
    print(f"\n user1 chose {user1_action}, user2 chose {user2_action}.\n")

    if user1_action == user2_action:
        print(f"Both players selected {user1_action}. It's a tie!")
    elif user1_action == "rock":
        if user2_action == "scissors":
            print("Rock smashes scissors! user1 win!")
        else:
            print("Paper covers rock! user2 win.")
    elif user1_action == "paper":
        if user2_action == "rock":
            print("Paper covers rock! uwer1 win!")
        else:
            print("Scissors cuts paper! uwer2 win.")
    elif user1_action == "scissors":
        if user2_action == "paper":
            print("Scissors cuts paper! uwer1 win!")
        else:
            print("Rock smashes scissors! user2 win.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
