HANGMAN_ASCII_ART = "  _    _                                         \n | |  | |                                        \n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                      __/ |                      \n                     |___/"
MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
print(MAX_TRIES)
letter_input = input("Guess a letter: ").lower()
print(letter_input)