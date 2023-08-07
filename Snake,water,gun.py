'''import random

def game():
    user_choice = input("Enter your choice (snake/water/gun): ").lower()
    computer_choice = random.choice(["snake", "water", "gun"])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "snake":
        if computer_choice == "water":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "water":
        if computer_choice == "gun":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "gun":
        if computer_choice == "snake":
            return "You win!"
        else:
            return "Computer wins!"
    else:
        return "Invalid input! Please enter snake, water, or gun."

# Main loop
while True:
    result = game()
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break'''


import random
def game():
        user_choice = input("Please Enter what you select(Snake/Water/Gun):").lower()
        computer_choice = random.choice(["snake", "water", "gun"])
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            return "It's tie"
        elif user_choice == "snake":
            if computer_choice =="water":
                return "You Are Winner"
            else:
                print("Computer WIN !")
        elif user_choice =="water":
            if computer_choice =="gun":
                return "You Are Winner"
            else:
                print("Computer WIN !")

        elif user_choice =="gun":
            if computer_choice =="snake":
                return "You Are Winner"
            else:
                print("Computer WIN !")
        else:
            return "Invalid input! Please enter snake, water, or gun."


while True:
    result = game()
    print(result)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break