def is_valid_guess(guess: str, length: int,unique_digits: bool = True) -> tuple[bool, str]:
    if len(guess) != length or " " in guess:
        return False, "The number must have 4 digits and no spaces."
    if not int(guess):
        return False, "The digit should consist entirely of numbers"
    if unique_digits:
        for i in range(len(guess) - 1):
            if sorted(guess)[i] == sorted(guess)[i + 1]:
                return False, "The number must have different digits"
    return True, "The number you entered is valid"


def is_new_guess(guess: str,history: set[str]) -> bool:
    return guess not in history

