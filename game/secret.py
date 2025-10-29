import random
def generate_secret(length: int = 4, unique_digits: bool = True, allow_leading_zero: bool = False) -> str:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    secret_number = ""
    for i in range(length):
        if not allow_leading_zero:
            if unique_digits:
                str_number = random.choice(numbers[1:])
                while str_number in secret_number:
                    str_number = random.choice(numbers[1:])
                secret_number += str_number
            else:
                secret_number += random.choice(numbers[1:])
        else:
            if unique_digits:
                str_number = random.choice(numbers)
                while str_number in secret_number:
                    str_number = random.choice(numbers)
                secret_number += str_number
            else:
                secret_number += random.choice(numbers)
    return secret_number



