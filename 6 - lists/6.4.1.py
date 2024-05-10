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