import random
from unittest import result


def create_code():
    """
    Function that creates the 4 digit code,
    using random digits from 1 to 8
        * returns a list of 4 integers
    """
    code = [0, 0, 0, 0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code


def show_instructions():
    """
    Shows instructions to the user
    """
    print(
        '4-digit Code has been set. Digits in range 1 to 8. \
You have 12 turns to break it.')


def show_results(result_tuple):
    """
    Show the results from one turn
    """
    print(
        'Number of correct digits in correct place:     ' +
     str(result_tuple[0]))
    print(
        'Number of correct digits not in correct place: ' +
     str(result_tuple[1]))

def get_answer_input():
    """
     Gets input from the user,
     and repeats this until the 
     input is exactly 4 characters
        * returns a 4 character string
    """
    answer = input("Input 4 digit code: ")
    if len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        return get_answer_input()
    return answer


def check_answer(code, answer):
    """
    Compares answer to pregenerated code,
    and returns a tuple containing (in this order):
        * correct digits in the correct position
        * correct digits not in the correct position
    """
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    return (
        correct_digits_and_position, 
        correct_digits_only
        )

def take_turn(code):
    """
    Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
       * returns a tuple containing (in this order):
            correct digits in the correct position,
            correct digits not in the correct position
    """
    answer = get_answer_input()
    result_tuple = check_answer(code, answer)
    show_results(result_tuple)
    return result_tuple

def show_code(code):
    """Show Code that was created to user"""
    print('The code was: '+str(code))


def check_correctness(
    turns,
    correct_digits_and_position
):
    """
    Checks correctness of answer and show output to user
        * returns a boolean 
    """

    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    print('Turns left: ' + str(12 - turns))
    return False


def run_game():
    """
    Main function for running the game,
    Starts a game of mastermind 
    """
    
    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        turns += 1
        if check_correctness(
            turns,
            take_turn(code)[0]
            ):
            break

    show_code(code)


if __name__ == "__main__":
    run_game()
