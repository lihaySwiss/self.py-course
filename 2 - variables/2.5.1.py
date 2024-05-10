import termcolor
HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
termcolor.cprint(HANGMAN_ASCII_ART, 'green')
termcolor.cprint('1:\n    x-------x','green')
termcolor.cprint('2:\n    x-------x\n    |\n    |\n    |\n    |\n    |','green')
termcolor.cprint('3:\n    x-------x\n    |       |\n    |       0\n    |\n    |\n    |\n','green')
termcolor.cprint('4:\n    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |\n','green')
termcolor.cprint('5:\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |\n    |\n','green')
termcolor.cprint('6:\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |\n','green')
termcolor.cprint('7:\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      / \\\n    |\n','green')
print(MAX_TRIES)
