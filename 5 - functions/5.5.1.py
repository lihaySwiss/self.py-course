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
def is_valid_input(letter_guessed):
    if (len(letter_input) > 1):
        return False
    elif (not letter_input.isalpha()):
        return False
    else:
        return True
    
def is_valid_input(letter_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha()

print(is_valid_input('abcd'))