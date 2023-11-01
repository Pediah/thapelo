import random
import time

def send_puzzle(message):
    puzzle = ''.join(chr(ord(char) + 1) if char.isalpha() else char for char in message)
    time.sleep(1)
    return puzzle

def receive_and_decode_puzzle(puzzle):
    decoded_message = ''.join(chr(ord(char) - 1) if char.isalpha() else char for char in puzzle)
    time.sleep(1)
    return decoded_message

def generate_access_code():
    return ''.join(random.sample("0123456789", 5))

def provide_hint(correct_code, user_guess):
    hints = []
    for i in range(5):
        if user_guess[i] == correct_code[i]:
            hints.append('C')
        elif user_guess[i] in correct_code:
            hints.append('N')
        else:
            hints.append('X')
    return hints

def unscramble_name_challenge(name):
    name_list = list(name)
    random.shuffle(name_list)
    return ''.join(name_list)

def play_unscramble_name_challenge(name, max_swaps):
    name_to_unscramble = unscramble_name_challenge(name)
    print(f"Unscramble the name: {name_to_unscramble}")

    for swap_count in range(1, max_swaps + 1):
        print(f"\nAttempt {swap_count}/{max_swaps}:")
        display_sequence(name_to_unscramble)
        
        pos1 = int(input("Enter the position of the first letter to swap: ")) - 1
        pos2 = int(input("Enter the position of the second letter to swap: ")) - 1
        
        if 0 <= pos1 < len(name) and 0 <= pos2 < len(name) and pos1 != pos2:
            # Swap the letters at the specified positions
            name_list = list(name_to_unscramble)
            name_list[pos1], name_list[pos2] = name_list[pos2], name_list[pos1]
            name_to_unscramble = ''.join(name_list)
            
            if name_to_unscramble == name:
                print("Congratulations! You unscrambled the name.")
                break
        else:
            print("Invalid input. Try again.")
    
    else:
        print(f"Sorry, you've reached the maximum number of swaps. The name remains unscrambled: {name}")

def present_riddles():
    print("\nCongratulations! Access granted. Here are five riddles for you:")
    
    riddles = [
        "I'm intangible, yet essential; you feel me but can't grasp me. What am I?",
        "I'm a complex potion of joy and pain, a force that binds and breaks. What am I?",
        "I'm a reflection in the pool of honesty, distorted by the waves of perception. What am I?",
        "I'm a gentle dance of connection, a whisper on the skin. What am I?",
        "I'm a delicate thread, woven through moments, holding the fabric of compassion. What am I?"
    ]

    answers = [
        "Breath",
        "Love",
        "Truth",
        "Kiss",
        "Care"
    ]

    for i, (riddle, answer) in enumerate(zip(riddles, answers), start=1):
        while True:
            user_answer = input(f"\nRiddle {i}: {riddle}\nYour answer: ").strip().lower()
            if user_answer == answer.lower():
                print("Correct! Proceed to the next riddle.")
                break
            else:
                print("Incorrect answer. Try again.")

    print("\nCongratulations! You've completed all the riddles.")

def display_sequence(sequence):
    print(' '.join(map(str, sequence)))

def play_game():
    accepted_name = "Thapelo"
    
    while True:
        user_name = input("Enter your full name: ").strip().capitalize()

        if user_name == accepted_name:
            break
        else:
            print("Access denied. Please enter your name.")

    print(f"Welcome, {user_name}!")

    play_unscramble_name_challenge(user_name, max_swaps=10)

    print("You've successfully unscrambled your name. Now, let's move on to the next stage.")


    encoded_message = send_puzzle("I know it's been a while and maybe you doubt a lot how much I care about you. \n Understandable, given how I react to things most times. \n I hope you enjoyed playing this thing that took me 3 days to code. Happy Birthday. ")
    print(f"\nSent Puzzle: {encoded_message}")

    access_code = generate_access_code()

    while True:
        user_guess = input("Guess the 5-digit passkey to unlock the message: \n *C- correct position* *X-invalid number* *N-wrong position* \n ")

        if len(set(user_guess)) == len(user_guess):
            if user_guess == access_code:
                print("Access granted! Now let's move on to the final challenge.")
                present_riddles()
                decoded_message = receive_and_decode_puzzle(encoded_message)
                print(f"\nDecoded Message: {decoded_message}")
                break
            else:
                hints = provide_hint(access_code, user_guess)
                print("Incorrect. Hints:", hints)
        else:
            print("Incorrect passkey. Please ensure there are no repeated digits. Try again.")

# Start the game
play_game()
