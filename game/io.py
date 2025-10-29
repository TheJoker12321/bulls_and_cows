def prompt_guess(length: int) -> str:
    guess_input = input(f"guess {length} numbers: ")
    return guess_input

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"Your guess is {guess}, bulls: {bulls} , cows: {cows} ")

def print_status(state: dict) -> None:
    print(f"your history: {state["history"]}")
    print(f"numbers guessed: {state["seen"]}")
    print(f"your tries are: {state["tries_used"]}")
    print(f"you have {state["max_tries"] - state["tries_used"]}")

def print_result(state: dict, won: bool) -> None:
    if won:
        print(f"You revealed the secret number. the number is {state["secret"]}")
    print(f"It's not a big deal, you lost. The secret number is: {state["secret"]}")
