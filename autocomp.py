import autocomplete
from pynput.keyboard import Key, Listener
import logging  # using module keyboard
import subprocess
import re
import numpy as np
#with open("big.txt") as file:
 # bob = str(file.read())
  #autocomplete.models.train_models(bob)

autocomplete.load()

curr_word = ""

def calculate_frequency(result):
    global curr_word
    total = np.zeros([26])
    for i in result:
        if i[0].__len__() > curr_word.__len__():
            string = i[0][curr_word.__len__()]
            #print("styr :" + string)
            total[ord(string)-97] += i[1]
    max = np.max(total)
    if max == 0:
        return total
    return total / max

def ignite(total):
    for i in range(0, 26):
        value = int(total[i] * 65535.0)
        valueh = "0x{:04x}".format(value)
        final_val = valueh[2:] + "00"
        #print(str(chr(i + 97)) + " : " + str(value) + " + " + final_val)
        #print(str(chr(i + 97)) + "Hex value: " + final_val)
        subprocess.call(["g810-led", '-kn', str(chr(i + 97)), final_val])
    subprocess.call(["g810-led", '-c'])

def other(string: str):
    for i in string:
        subprocess.call(["g810-led", '-k', i, 'FF0000'])
    subprocess.call(["g810-led", '-k', 'alt', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'left', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'right', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'top', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'bottom', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'shift', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'space', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'f4', 'FF0000'])
    subprocess.call(["g810-led", '-k', 'f1', 'FF0000'])

def display():
    global curr_word
    #print(curr_word)
    result = autocomplete.predict_currword(curr_word, top_n=1000)
    #print(result)
    total = calculate_frequency(result)
    #bn print(str(total) + "\n")
    ignite(total)

def on_press(key):
    global curr_word
    subprocess.call(["g810-led", '-a', '000000'])
    try:
        if key == Key.space:
                curr_word = ""
        elif key == Key.ctrl:
            other("nxcvarsflp")
        elif re.search("[a-z]", key.char):
            curr_word = curr_word + key.char
            display()
    except:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
