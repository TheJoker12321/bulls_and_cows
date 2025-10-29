from game.io import prompt_guess, print_feedback, print_status, print_result
from game.logic import game_state, is_won, apply_guess
from game.secret import generate_secret
from game.validate import is_valid_guess, is_new_guess


def play(length: int = 4, max_tries: int | None = 12, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    secret_number = generate_secret()
    data = game_state(secret_number, unique_digits, allow_leading_zero, length, max_tries)
    while data["max_tries"] - data["tries_used"] >= 1:
        guess = prompt_guess(length)
        valid = is_valid_guess(guess, length, unique_digits)
        if not valid[0]:
            print(valid[1])
            continue
        if not is_new_guess(guess, data["seen"]):
            print("You have already guessed this number, try again...")
            continue
        result = apply_guess(data, guess)
        print_feedback(guess, result[0], result[1])
        bulls = result[0]
        print_status(data)
        if is_won(bulls, length):
            print_result(data, True )
            break
    if data["max_tries"]  - data["tries_used"] == 0:
        print_result(data, False )





if __name__ == "__main__":
    play()