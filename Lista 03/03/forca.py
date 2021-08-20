from random import randint
import os
import time

def Forca(tentativa): 
    forca = [
    '''
    ____________
    |           |
    |           
    |
    |
    |
    |
    ---''',

    '''
    ____________
    |           |
    |           O
    |
    |
    |
    |
    ---''',

    '''
    ____________
    |           |
    |           O
    |           |
    |
    |
    |
    ---''',

    '''
    ____________
    |           |
    |           O
    |          /|
    |
    |
    |
    ---''',

    '''
    ____________
    |           |
    |           O
    |          /|\\
    |
    |
    |
    ---''',

    '''
    ____________
    |           |
    |           O
    |          /|\\
    |          / 
    |
    |
    ---''',

    '''
    ____________
    |           |
    |           O
    |          /|\\
    |          / \\
    |
    |
    ---''',

    ]


    """  for i in range(tentativa + 1):
        print(forca[i])
        time.sleep(1)
        os.system('cls')     """
    print(forca[tentativa])
    time.sleep(1)
    os.system('cls')  

