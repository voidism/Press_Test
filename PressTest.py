import pyautogui
import os
import re
import time

i = raw_input("Test File Name:")

if not os.path.exists(i):
    print "Test File Not Found!"
else:
    f = open(i)
    ftxt = f.read()
    cmds = ftxt.split('\n')

    print "\nYou have 10 seconds to click the target window ..."
    for i in range(10):
        print "\r ...", 10-i-1,
        time.sleep(1)
    print '\n'
    idx = 0
    gex = re.compile(r'Key(\w*) \"*([0-9A-Za-z+-@# !\%\$\^&\*]*)\"*, (\d)')
    for cmd in cmds:
        print "["+str(idx)+"]",
        try:
            gex.search(cmd).group()
            idx+=1
        except:
            break

        act = gex.search(cmd).group(1)
        key = gex.search(cmd).group(2).lower()
        times = int(gex.search(cmd).group(3))

        if key == 17:
            key = 'ctrl'
        elif key == 65:
            key = 'a'
        elif key == ' ':
            key = 'space'

        print act, key, times

        if act == 'Press':
            for i in range(times):
                pyautogui.press(key)

        if act == 'Down':
            for i in range(times):
                pyautogui.keyDown(key)

        if act == 'Up':
            for i in range(times):
                pyautogui.keyUp(key)

os.system("pause")

