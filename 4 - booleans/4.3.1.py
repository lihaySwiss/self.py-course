HANGMAN_ASCII_ART = "  _    _                                         \n | |  | |                                        \n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                      __/ |                      \n                     |___/"
MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
print(MAX_TRIES)
letter_input = input("Guess a letter: ")

if len(letter_input) > 1 and not letter_input.isalpha():
    print("E3")
elif len(letter_input) > 1:
    print("E1")
elif not letter_input.isalpha():
    print("E2")
else:
    print(letter_input.lower())


