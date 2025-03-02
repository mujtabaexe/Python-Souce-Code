import random  # Import the random module for generating random numbers and choices

users = []  # List to store user details
calc_uses = 0  # Counter for the total number of calculator uses
hangman_plays = 0  # Counter for the total number of Hangman game plays
hangman_wins = 0  # Counter for the total number of Hangman game wins
guess_plays = 0  # Counter for the total number of Guess game plays
guess_wins = 0  # Counter for the total number of Guess game wins
rps_plays = 0  # Counter for the total number of Rock Paper Scissors game plays
rps_wins = 0  # Counter for the total number of Rock Paper Scissors game wins
rps_draws = 0  # Counter for the total number of Rock Paper Scissors game draws

while True:  # Outer loop to manage multiple users
    user_name = input("Enter your name: ")  # Prompt the user to enter their name
    user_summary = {  # Dictionary to store the current user's summary
        'name': user_name,
        'calc_uses': 0,
        'hangman_plays': 0,
        'hangman_wins': 0,
        'hangman_losses': 0,
        'guess_plays': 0,
        'guess_wins': 0,
        'guess_losses': 0,
        'rps_plays': 0,
        'rps_wins': 0,
        'rps_losses': 0,
        'rps_draws': 0
    }
    users.append(user_summary)  # Add the current user's summary to the list of users
    
    while True:  # Inner loop to manage multiple operations for the current user
        try:
            operation = int(input("\nEnter 1 for Calculator, 2 for Hangman game, 3 for Guess game, 4 for Rock Paper Scissors game, or 0 to exit the program: "))  # Prompt user for operation
        except ValueError:  # Handle invalid input
            print("Invalid input! Please enter a valid option.")
            continue

        if operation < 0 or operation > 4:  # Check for valid operation input
            print("Invalid input! Please enter a valid option.")
            continue

        if operation == 0:  # Exit the program
            print("You have successfully exited the program")
            break

        elif operation == 1:  # Calculator functionality
            calc_uses += 1  # Increment the total calculator uses counter
            user_summary['calc_uses'] += 1  # Increment the current user's calculator uses counter
            while True:  # Loop to manage multiple calculator operations
                try:
                    operation = int(input("\nEnter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, and 0 to exit: "))  # Prompt user for calculator operation
                except ValueError:  # Handle invalid input
                    print("Invalid input! Please enter a valid option.")
                    continue
                if operation < 0 or operation > 4:  # Check for valid operation input
                    print("Invalid input! Please enter a valid option.")
                    continue
                if operation == 0:  # Exit the calculator
                    print("You have successfully exited the \"Calculator\"")
                    break

                try:
                    num1 = eval(input("Enter your first number: "))  # Prompt user for first number
                    num2 = eval(input("Enter your second number: "))  # Prompt user for second number
                except (SyntaxError, NameError):  # Handle invalid number input
                    print("Invalid input! Please enter valid numbers.")
                    continue

                if operation == 1:  # Addition operation
                    print("Addition of", num1, "and", num2, "is:", num1 + num2)
                elif operation == 2:  # Subtraction operation
                    print("Difference between", num1, "and", num2, "is:", num1 - num2)
                elif operation == 3:  # Multiplication operation
                    print("Product of", num1, "and", num2, "is:", num1 * num2)
                elif operation == 4:  # Division operation
                    if num2 == 0:  # Check for division by zero
                        while num2 == 0:  # Loop until a valid second number is entered
                            print("Cannot be divided by zero")
                            try:
                                num2 = eval(input("Enter second number again: "))  # Prompt user for a valid second number
                            except (SyntaxError, NameError):  # Handle invalid number input
                                print("Invalid input! Please enter a valid number.")
                                continue
                            if num2 != 0:  # Perform division if the second number is valid
                                print("Division of", num1, "by", num2, "is:", num1 / num2)
                    else:  # Perform division if the second number is valid
                        print("Division of", num1, "by", num2, "is:", num1 / num2)

        elif operation == 2:  # Hangman game functionality
            hangman_plays += 1  # Increment the total Hangman plays counter
            user_summary['hangman_plays'] += 1  # Increment the current user's Hangman plays counter
            list1 = ["snakes", "planks", "excellent", "message", "dracula", "serpant", "invoke", "construct", "deplore", "imagine"]  # List of words for Hangman
            length = len(list1) - 1  # Length of the word list

            games = 1  # Initialize the number of games played
            wins = 0  # Initialize the number of wins
            losses = 0  # Initialize the number of losses
            tries = 0  # Initialize the number of tries
            while True:  # Loop to manage multiple Hangman games
                dashes = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]  # Placeholder for the word to guess
                n = random.randint(0, length)  # Randomly select a word from the list
                word = list1[n]  # The word to guess
                letters = list(word)  # List of letters in the word
                letter_length = len(letters)  # Length of the word
                print(f"The word has {len(word)} letters")  # Print the number of letters in the word
                new_dash = None  # Placeholder for the updated dashes
                user_guess = []  # List to store user's guesses
                while tries < 6:  # Allow up to 6 incorrect guesses
                    correct = True  # Initialize the correctness of the guess
                    while correct:  # Loop to ensure valid input
                        guess = input("Enter a letter: ")  # Prompt user for a letter
                        if len(guess) == 1:  # Check for valid input
                            correct = False  # Exit the loop if input is valid
                        elif guess == "":  # Handle empty input
                            print("Invalid input! Please enter a single letter only.")
                        else:  # Handle invalid input
                            print("Enter a single letter only")

                    for i, j in enumerate(letters):  # Loop through the letters in the word
                        if j == guess.lower():  # Check if the guessed letter is in the word
                            idx = i  # Get the index of the guessed letter
                            dashes[idx] = guess.lower()  # Update the dashes with the guessed letter

                    new_dash = dashes[0:letter_length]  # Update the placeholder for the dashes
                    print(new_dash)  # Print the updated dashes

                    if guess in user_guess:  # Check if the letter was already guessed
                        tries -= 1  # Decrement the tries counter if the letter was already guessed
                    tries += 1  # Increment the tries counter
                    user_guess.append(guess)  # Add the guessed letter to the list of guesses
                    if guess in dashes:  # Check if the guessed letter is in the dashes
                        tries -= 1  # Decrement the tries counter if the guessed letter is in the dashes
                        user_guess.remove(guess)  # Remove the guessed letter from the list of guesses

                    if new_dash == letters:  # Check if the user guessed the word correctly
                        wins += 1  # Increment the wins counter
                        hangman_wins += 1  # Increment the total Hangman wins counter
                        user_summary['hangman_wins'] += 1  # Increment the current user's Hangman wins counter
                        break  # Exit the loop

                    print(f"You have {6 - tries} guesses left")  # Print the number of guesses left

                if new_dash != letters:  # Check if the user didn't guess the word correctly
                    losses += 1  # Increment the losses counter
                    user_summary['hangman_losses'] += 1  # Increment the current user's Hangman losses counter

                print(f"The word was {word}")  # Print the word to guess
                again = input("\nDo you want to play again? Enter 'y' or enter any other alphabet \nor simply press \"Enter\" to exit to the \"Main Menu\": ")  # Prompt to play again
                if again.lower() == "y":  # Check if the user wants to play again
                    tries = 0  # Reset the tries counter
                    games += 1  # Increment the games counter
                else:  # Exit to the main menu
                    break

            print(f"You played {games} and won {wins}")  # Print the number of games played and won

        elif operation == 3:  # Guess game functionality
            while True:  # Loop to manage multiple Guess games
                guess_plays += 1  # Increment the total Guess plays counter
                user_summary['guess_plays'] += 1  # Increment the current user's Guess plays counter
                num = random.randint(1, 20)  # Generate a random number between 1 and 20
                count = 0  # Initialize the number of attempts

                while count < 5:  # Allow up to 5 attempts
                    try:
                        a = int(input("Enter an integer between 1 and 20: "))  # Prompt user for an integer
                    except ValueError:  # Handle invalid input
                        print("Invalid input! Please enter a valid integer.")
                        continue
                    count += 1  # Increment the attempts counter
                    if a > num:  # Check if the guess is too high
                        print("\nSelect a smaller number")
                    elif a < num:  # Check if the guess is too low
                        print("\nSelect a greater number")
                    else:  # Check if the guess is correct
                        print("\nCongratulations!!! You guessed the correct number.")
                        print("You guessed the correct number after", count, "attempts.")
                        guess_wins += 1  # Increment the total Guess wins counter
                        user_summary['guess_wins'] += 1  # Increment the current user's Guess wins counter
                        break

                if count == 5 and a != num:  # Check if the user used all attempts and didn't guess correctly
                    print(f"Sorry, you've used all 5 attempts. The correct number was {num}.")
                    user_summary['guess_losses'] += 1  # Increment the current user's Guess losses counter

                again = input("\nDo you want to play again? Enter 'y' to play again or enter any other alphabet \nor simply press \"Enter\" to exit to the \"Main Menu\": ")  # Prompt to play again
                if again.lower() != "y":  # Check if the user wants to exit to the main menu
                    break

        elif operation == 4:  # Rock Paper Scissors game functionality
            while True:  # Loop to manage multiple Rock Paper Scissors games
                rps_plays += 1  # Increment the total Rock Paper Scissors plays counter
                user_summary['rps_plays'] += 1  # Increment the current user's Rock Paper Scissors plays counter

                rock = """
                    _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)
                """  # ASCII art for rock

                paper = """
                    _______
                ---'   ____)____
                          ______)
                          _______)
                         _______)
                ---.__________)
                """  # ASCII art for paper

                scissors = """
                    _______
                ---'   ____)____
                          ______)
                       __________)
                      (____)
                ---.__(___)
                """  # ASCII art for scissors

                def getcomp_choice():  # Function to get computer's choice
                    choices = ["rock", "paper", "scissors"]  # List of choices
                    return random.choice(choices)  # Randomly select a choice

                def getuser_choice():  # Function to get user's choice
                    enter = input("Enter your choice (rock, paper, scissors): ").lower()  # Prompt user for choice
                    while enter not in ["rock", "paper", "scissors"]:  # Check for valid input
                        if enter == "":  # Handle empty input
                            print("Invalid input! Please enter a correct choice.")
                        else:  # Handle invalid input
                            print("Choice is invalid, please enter a correct choice.")
                        enter = input("Enter your choice (rock, paper, scissors): ").lower()  # Prompt user for valid input
                    return enter  # Return user's choice

                def winner(user_choice, comp_choice):  # Function to determine the winner
                    if user_choice == comp_choice:  # Check for draw
                        return "It's a draw"
                    elif (user_choice == "rock" and comp_choice == "scissors") or (user_choice == "paper" and comp_choice == "rock") or (user_choice == "scissors" and comp_choice == "paper"):  # Check if user wins
                        return "You win"
                    else:  # User loses
                        return "You lost"

                def game_start():  # Function to start the Rock Paper Scissors game
                    global rps_wins, rps_draws, rps_plays  # Access global counters
                    print("Welcome to rock, paper, and scissors")  # Welcome message
                    games_played = 0  # Initialize the number of games played
                    games_won = 0  # Initialize the number of games won
                    games_drawn = 0  # Initialize the number of games drawn
                    games_lost = 0  # Initialize the number of games lost
                    while True:  # Loop to manage multiple Rock Paper Scissors games
                        user_choice = getuser_choice()  # Get user's choice
                        comp_choice = getcomp_choice()  # Get computer's choice

                        print(f"You choose: {user_choice}")  # Print user's choice
                        if user_choice == "rock":  # Print ASCII art for user's choice
                            print(rock)
                        elif user_choice == "scissors":
                            print(scissors)
                        elif user_choice == "paper":
                            print(paper)

                        print(f"Computer chose: {comp_choice}")  # Print computer's choice
                        if comp_choice == "rock":  # Print ASCII art for computer's choice
                            print(rock)
                        elif comp_choice == "scissors":
                            print(scissors)
                        elif comp_choice == "paper":
                            print(paper)

                        result = winner(user_choice, comp_choice)  # Determine the winner
                        print(result)  # Print the result

                        if result == "You win":  # Check if user wins
                            games_won += 1  # Increment the games won counter
                            rps_wins += 1  # Increment the total Rock Paper Scissors wins counter
                            user_summary['rps_wins'] += 1  # Increment the current user's Rock Paper Scissors wins counter
                        elif result == "It's a draw":  # Check if it's a draw
                            games_drawn += 1  # Increment the games drawn counter
                            rps_draws += 1  # Increment the total Rock Paper Scissors draws counter
                            user_summary['rps_draws'] += 1  # Increment the current user's Rock Paper Scissors draws counter
                        else:  # User loses
                            games_lost += 1  # Increment the games lost counter
                            user_summary['rps_losses'] += 1  # Increment the current user's Rock Paper Scissors losses counter
                        
                        games_played += 1  # Increment the games played counter

                        playagain = input("\nDo you want to play again? Enter 'y' to play again or enter any other alphabet \nor simply press \"Enter\" to exit to the \"Main Menu\": ")  # Prompt to play again
                        if playagain.lower() != "y":  # Check if the user wants to exit to the main menu
                            break

                    print("Thanks for playing")  # Thank the user for playing
                    print(f"Total games played: {games_played}")  # Print the total games played
                    print(f"Total games won: {games_won}")  # Print the total games won
                    print(f"Total games drawn: {games_drawn}")  # Print the total games drawn
                    print(f"Total games lost: {games_lost}")  # Print the total games lost

                game_start()  # Start the Rock Paper Scissors game
                break
        
    another_user = input("\nDoes another person want to use the program? Enter 'y' for yes \nor enter any other alphabet or simply press \"Enter\" to exit the program: ")  # Prompt for another user
    if another_user.lower() != "y":  # Check if another user wants to use the program
        break

print("\nSummary of your activity:")  # Print the summary of activities
for user in users:  # Loop through each user
    print(f"\nUser: {user['name']}")  # Print user's name
    print(f"Calculator used: {user['calc_uses']} times")  # Print the number of times the calculator was used
    print(f"Hangman played: {user['hangman_plays']} times, Wins: {user['hangman_wins']}, Losses: {user['hangman_losses']}")  # Print the number of Hangman plays, wins, and losses
    print(f"Guess game played: {user['guess_plays']} times, Wins: {user['guess_wins']}, Losses: {user['guess_losses']}")  # Print the number of Guess game plays, wins, and losses
    print(f"Rock Paper Scissors played: {user['rps_plays']} times, Wins: {user['rps_wins']}, Draws: {user['rps_draws']}, Losses: {user['rps_losses']}")  # Print the number of Rock Paper Scissors plays, wins, draws, and losses
