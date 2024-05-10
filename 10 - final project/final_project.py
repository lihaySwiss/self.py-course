HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
old_letters_guessed = []
HANGMAN_PHOTOS = {1: """    x-------x""",
                  2: """    x-------x
    |
    |
    |
    |
    |""",
                  3: """    x-------x
    |       |
    |       0
    |
    |
    |
""",
                  4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
                  5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""",
                  6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / 
    |
""",
                  7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""

                  }


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS.get(num_of_tries))


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Function will return a string with underlines and letters guessed
    :param secret_word: secret word
    :param old_letters_guessed: given list
    :return: string with underlines and letters guessed
    """
    display_string = ""
    for i in range(len(secret_word)):
        if (secret_word[i] in old_letters_guessed):
            display_string += secret_word[i] + " "
        else:
            display_string += "_ "
    display_string = display_string[:-1]
    return display_string


def check_win(secret_word, old_letters_guessed):
    """
    Function will check if secret word is completed
    :param secret_word: secret word
    :param old_letters_guessed: given list of old letters
    :return: True if secret word is completed / False if not
    """
    for i in range(len(secret_word)):
        if (secret_word[i] not in old_letters_guessed):
            return False
    return True


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Function will check if letter is valid (and if it already exists in list)
    :param letter_guessed: given letter
    :param old_letters_guessed: given list
    :return: True / False
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        old_letters_guessed += letter_guessed
        old_letters_guessed = update_old_letters(old_letters_guessed)
        return True

def update_old_letters(old_letters_guessed):
    old_letters_guessed = sorted(old_letters_guessed)
    old_letters_guessed = str(old_letters_guessed)[1:-1].replace(", ", " -> ")
    old_letters_guessed = old_letters_guessed.replace("'", "")
    return old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """
    Function will print message if letter exists in current list
    :param letter_guessed: current letter given
    :param old_letters_guessed: given list
    :return: True/False
    :rtype: bool
    """
    old_letters_guessed = update_old_letters(old_letters_guessed)
    if letter_guessed not in secret_word:
        print(":(")
        return False
    print(":)")
    return True


def choose_word(file_path, index):
    file = open(file_path, 'r').read().split(' ')
    exist = []

    for word in file:
        if word not in exist:
            exist.append(word)
    if index > len(file):
        while index > len(file):
            index -= len(file)
    return (len(exist), file[index - 1])


def main():
    print(HANGMAN_ASCII_ART)
    file_path = input("Enter words file path: ")
    word_index = int(input("Enter word index (starts from 1): "))
    print("Lets start!\n")
    secret_word = choose_word(file_path, word_index)[1]
    old_letters_guessed = []
    letter_guess = ''
    num_of_tries = 1
    print_hangman(num_of_tries)
    while not check_win(secret_word, old_letters_guessed):
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guess = input("Enter letter guess: ")
        while not check_valid_input(letter_guess, old_letters_guessed):
            print("X")
            print(update_old_letters(old_letters_guessed))
            letter_guess = input("Enter letter guess: ")
        if not try_update_letter_guessed(letter_guess, old_letters_guessed, secret_word):
            num_of_tries += 1
            print_hangman(num_of_tries)
        if num_of_tries > MAX_TRIES:
            print(show_hidden_word(secret_word, old_letters_guessed))
            print("LOSE")
            break
            return None
    if num_of_tries <= MAX_TRIES:
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("WIN")

if __name__ == "__main__":
    main()
