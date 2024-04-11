def get_secret_number(player):
    while True:
        secret_number = input("{}: Set your multi-digit number: ".format(player))
        if secret_number.isdigit():
            return secret_number
        else:
            print("Please enter a valid multi-digit number.")

def get_guess(player):
    guess = input("{}: Enter your guess: ".format(player))
    return guess

def evaluate_guess(secret_number, guess):
    correct_digits = sum(1 for s, g in zip(secret_number, guess) if s == g)
    return correct_digits


def play_mastermind_two_players():
    secret_number_Arun = get_secret_number("Arun")
    print("Moses, try to guess Arun's number!")

    attempts_Moses = 0
    while True:
        guess_Moses = get_guess("Moses")

        attempts_Moses += 1
        correct_digits = evaluate_guess(secret_number_Arun, guess_Moses)

        if correct_digits == len(secret_number_Arun):
            print("Moses wins! They guessed the number {} in {} attempts.".format(secret_number_Arun, attempts_Moses))
            return

        print("Hint: {} digits are correct.".format(correct_digits))

        secret_number_Moses = get_secret_number("Moses")
        print("Arun, try to guess Moses's number!")

        attempts_Arun = 0
        while True:
            guess_Arun = get_guess("Arun")

            attempts_Arun += 1
            correct_digits = evaluate_guess(secret_number_Moses, guess_Arun)

            if correct_digits == len(secret_number_Moses):
                print("Arun wins! They guessed the number {} in {} attempts.".format(secret_number_Moses, attempts_Arun))
                return

            print("Hint: {} digits are correct.".format(correct_digits))
play_mastermind_two_players()
