import random
import time

def start_game():
    """
    This function starts the game and introduces the player to the scenario.
    """
    print("Welcome to the adventure game!")
    print("You are standing at the entrance of a dark cave.")
    print("You have a flashlight with weak batteries.")
    print("You need to find a way out of the cave before your flashlight runs out.")
    time.sleep(2)  # Create a delay before the game starts

def display_score(total_score):
    """
    This function displays the player's current score.
    """
    print("Your current score is: " + str(total_score))

def move_forward(total_score):
    """
    This function handles the player's decision to move forward.
    """
    print("You move forward, but the path is unclear.")
    time.sleep(1)
    if random.random() < 0.5:
        print("You stumble and fall, wasting 2 minutes of battery life.")
        total_score -= 2
    else:
        print("You find a path that looks promising.")
        if random.random() < 0.2:
            print("You find the cave exit!")
            return total_score, True
    return total_score, False

def search_for_side_room(total_score):
    """
    This function handles the player's decision to search for a side room.
    """
    print("You search for a side room and find one.")
    time.sleep(1)
    if random.random() < 0.7:
        print("You find a battery pack and recharge your flashlight for 5 minutes.")
        total_score += 5
    else:
        print("You find nothing useful.")
    return total_score, False

def try_to_fix_flashlight(total_score):
    """
    This function handles the player's decision to try to fix the flashlight.
    """
    print("You try to fix your flashlight, but it's not easy.")
    time.sleep(1)
    if random.random() < 0.3:
        print("You manage to fix it and gain 3 minutes of battery life.")
        total_score += 3
    else:
        print("You fail to fix it and waste 1 minute of battery life.")
        total_score -= 1
    return total_score, False

def play_again():
    """
    This function asks the player if they want to play again.
    """
    response = input("Do you want to play again? (Y/N) ")
    if response.upper() == "Y":
        start_game()
        play_game()
    else:
        print("Thanks for playing!")

def play_game():
    """
    This function contains the main game loop.
    """
    total_score = 10  # Initialize total score
    cave_exit_found = False  # Initialize cave exit found flag

    while not cave_exit_found and total_score > 0:
        print("\nYou have " + str(total_score) + " minutes of flashlight battery left.")
        display_score(total_score)
        action = input("Do you want to (A) move forward, (B) search for a side room, or (C) try to fix your flashlight? ")

        if action.upper() == "A":
            total_score, cave_exit_found = move_forward(total_score)
        elif action.upper() == "B":
            total_score, cave_exit_found = search_for_side_room(total_score)
        elif action.upper() == "C":
            total_score, cave_exit_found = try_to_fix_flashlight(total_score)
        else:
            print("Invalid input. Please try again.")
            time.sleep(1)
            continue

        if cave_exit_found:
            print("Congratulations, you found the cave exit!")
        elif total_score <= 0:
            print("Sorry, your flashlight ran out of battery. Game over.")

    play_again()

start_game()
play_game()
