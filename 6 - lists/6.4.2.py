HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
print(MAX_TRIES)
old_letters_guessed = []
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Function will check if letter is valid (and if it already exists in list)
    :param letter_guessed: given letter
    :param old_letters_guessed: given list
    :return: True / False
    """
    letter_guessed = letter_guessed.lower()
    if (len(letter_guessed) > 1):
        return False
    elif (not letter_guessed.isalpha()):
        return False
    elif (letter_guessed in old_letters_guessed):
        return False
    else:
        old_letters_guessed += letter_guessed
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Function will print message if letter exists in current list
    :param letter_guessed: current letter given
    :param old_letters_guessed: given list
    :return: True/False
    :rtype: bool
    """
    if(not check_valid_input(letter_guessed,old_letters_guessed)):
        old_letters_guessed = sorted(old_letters_guessed)
        old_letters_guessed = str(old_letters_guessed)[1:-1].replace(", ", " -> ")
        old_letters_guessed = old_letters_guessed.replace("'", "")
        print("X")
        print(old_letters_guessed)
        return False
    else:
        return True
try_update_letter_guessed('a',['a', 'c', 'b'])