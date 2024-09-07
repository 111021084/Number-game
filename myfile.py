import random


def number_game(difficulty="easy"):
    if difficulty == "easy":
        max_attempts = 10
        range_start = 1
        range_end = 100
    elif difficulty == "medium":
        max_attempts = 7
        range_start = 1
        range_end = 200
    elif difficulty == "hard":
        max_attempts = 5
        range_start = 1
        range_end = 500
    else:
        print("Invalid difficulty level.")
        return

    insert_number = random.randint(range_start, range_end)
    attempts = 0

    while attempts < max_attempts:
        try:
            number = int(input(f"Insert a number between {range_start} and {range_end}: "))
            if not (range_start <= number <= range_end):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number within the specified range.")
            continue

        if number == insert_number:
            return f"You won the game in {attempts + 1} attempt(s)!"
        elif number < insert_number:
            print("The number is higher.")
        else:
            print("The number is lower.")
        attempts += 1

    return f"Game Over. You used all {max_attempts} attempts. The number was {insert_number}."


results = number_game("easy")
print(results)
