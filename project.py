import random
import image

user_score = 0
computer_score = 0
while True:
    user_action = input("Enter a choice (r for rock,p for paper,s for scissorr): ")
    possible_actions = ["r", "p", "s"]
    if user_action not in possible_actions:
        print("Invalid input")
    else:
        computer_action = random.choice(possible_actions)
        print("You chose:", user_action)
        image.check(user_action)
        print("computer chose ", computer_action)
        image.check(computer_action)

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "r":
            if computer_action == "s":
                print("Rock smashes scissors! You win!")
                user_score += 1
            else:
                print("Paper covers rock! You lose.")
                computer_score += 1
        elif user_action == "p":
            if computer_action == "r":
                print("Paper covers rock! You win!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_score += 1
        elif user_action == "s":
            if computer_action == "p":
                print("Scissors cuts paper! You win!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_score += 1
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
print("       scores       ")
print("CPU : ", computer_score)
print("YOU : ", user_score)
