import subprocess

def other():
    orange = "ffa500"
    for i in """qaz1~<p[]';/0-=\\\\""":
        subprocess.call(["g810-led", '-k', i, orange])
    subprocess.call(["g810-led", '-k', 'tab', orange])
    subprocess.call(["g810-led", '-k', 'capslock', orange])
    subprocess.call(["g810-led", '-k', 'shiftl', orange])
    subprocess.call(["g810-led", '-k', 'ctrll', orange])

    subprocess.call(["g810-led", '-k', 'shiftr', orange])
    subprocess.call(["g810-led", '-k', 'ctrlr', orange])
    subprocess.call(["g810-led", '-k', 'winl', orange])


    subprocess.call(["g810-led", '-k', 'backslash', orange])
    subprocess.call(["g810-led", '-k', 'dollar', orange])

    subprocess.call(["g810-led", '-k', 'quote', orange])

    subprocess.call(["g810-led", '-k', 'enter', orange])

    subprocess.call(["g810-led", '-k', 'winr', orange])

    subprocess.call(["g810-led", '-k', 'menu', orange])

    subprocess.call(["g810-led", '-k', 'backspace', orange])

    subprocess.call(["g810-led", '-k', 'fn', orange])
    for i in '2wsx':
        subprocess.call(["g810-led", '-k', i, '800080'])
    for i in '3edc':
        subprocess.call(["g810-led", '-k', i, 'ff007f'])
    for i in '45rtfgvb':
        subprocess.call(["g810-led", '-k', i, 'ff0000'])
    for i in '67yuhjnm':
        subprocess.call(["g810-led", '-k', i, 'ffff00'])
    for i in '8ik,':
        subprocess.call(["g810-led", '-k', i, '00ffff'])
    for i in '9ol.':
        subprocess.call(["g810-led", '-k', i, '0000ff'])
    subprocess.call(["g810-led", '-k', 'space', '7f00ff'])
    subprocess.call(["g810-led", '-k', 'altl', '7f00ff'])
    subprocess.call(["g810-led", '-k', 'altr', '7f00ff'])

other()
