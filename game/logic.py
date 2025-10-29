from game.secret import generate_secret


def score_guess(secret: str, guess: str) -> tuple[int, int]:
    count_bull = 0
    count_cows = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            count_bull += 1
        else:
            if guess[i] in secret:
                count_cows += 1
    return count_bull, count_cows

def is_won(bulls: int, length: int) -> bool:
    return bulls == length

def game_state(secret: str , unique_digits: bool, allow_leading_zero: bool, length = 4, max_tries = int | None) -> dict:
    data_game = {
        "secret": secret ,
        "length": length,
        "max_tries": max_tries,
        "tries_used": 0,
        "unique_digits": unique_digits,
        "allow_leading_zero": allow_leading_zero,
        "history": list(),
        "seen": set()
    }
    return data_game

def apply_guess(state: dict, guess: str) -> tuple[int, int]:
    check = score_guess(state["secret"], guess)
    tap_history = (guess, check[0], check[1])
    state["history"].append(tap_history)
    state["tries_used"] += 1
    state["seen"].add(guess)
    return check
