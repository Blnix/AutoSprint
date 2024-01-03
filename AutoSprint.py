import time
import json
import keyboard
import random
from datetime import datetime

large_text = '''
 _____      ________              _____       _____         
___    |___  ___  /________  ___/_________________(_)________  /_        
__  /| |  / / /  __/  __ \____ \___  __ \_  ___/_  /__  __ \  __/        
_  ___ / /_/ // /_ / /_/ /___/ /__  /_/ /  /   _  / _  / / / /_          
/_/  |_\__,_/ \__/ \____//____/ _  .___//_/    /_/  /_/ /_/\__/          
                                /_/                                      
'''
print(large_text)
with open('sprintconfig.json') as f:
    data = json.load(f)

delay = data.get('delay')
if not delay == "r":    
    delay = float(delay)

ctrl = False
pause = False
print("Made by Blnix.")
print("AutoSprint is running, waiting for input.")
print("")

def on_w_press(e):
    global ctrl
    global pause
    if pause == False:
        if not ctrl:
            print(datetime.now().strftime('%H:%M:%S:%f'),": W pressed.")
            if delay == "r":
                randomdelay = 0.11 + random.randrange(1, 100) * 0.00025
                randomdelay = float(randomdelay)
                time.sleep(randomdelay)
                print(datetime.now().strftime('%H:%M:%S:%f'), ": Delay:", randomdelay)

            else:
                time.sleep(delay)
            print(datetime.now().strftime('%H:%M:%S:%f'), ": CTRL pressed.")
            keyboard.press('ctrl')
            ctrl = True

def on_w_release(e):
    global ctrl
    global pause
    if pause == False:
        if ctrl:
            print(datetime.now().strftime('%H:%M:%S:%f'), ": CTRL released.")
            print("")
            keyboard.release('ctrl')
            ctrl = False

def scriptpause(e):
    global pause
    global ctrl
    if pause == False:
        pause = True
        print(datetime.now().strftime('%H:%M:%S:%f'),": Script paused.")
    elif pause == True:
        pause = False
        ctrl = False
        print(datetime.now().strftime('%H:%M:%S:%f'),": Script resumed.")

keyboard.on_press_key('w', on_w_press)
keyboard.on_release_key('w', on_w_release)
keyboard.on_release_key('k', scriptpause)
keyboard.wait('l')
print("Exiting script due to user.")
