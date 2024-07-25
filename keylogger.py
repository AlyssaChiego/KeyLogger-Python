from pynput import keyboard

# prints typed key in terminal
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
