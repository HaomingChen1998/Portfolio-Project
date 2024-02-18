errorMessage = "Some error occurred, make sure you have all the required libraries installed from requirements.txt"

print('>> Importing Libraries')
try:
    import pyautogui
    import time
    import sys
    from datetime import datetime
    from random import randint
    from tqdm import tqdm
    import ctypes
    
except Exception as exp:
    print (f'>><< Error: {exp}')
    print(errorMessage)
    exit()
print('>> Libraries Imported')

print('>> Setting Up')
try:
    pyautogui.FAILSAFE = False
    waitTime = 1
    try:
        waitTime = max(1, int(sys.argv[-1]))
    except Exception as exp:
        pass
    prevousLocation = None
    print(f'>> Wait time set to: {waitTime*5} seconds')
except Exception as exp:
    print (f'>><< Error: {exp}')
    print(errorMessage)
    exit()
print(f'>> Setup Complete')


def hasMoved(currentLocation):
    try:
        time.sleep(randint(0,2))
        if pyautogui.position() == currentLocation:
            return False
        else:
            print('>> Input detected, interrupting stay-awake')
            return True
    except Exception as exp:
        print(f'>><< Error: {exp}')
        print(errorMessage)
        exit()


        
def stay_awake_actions():
    # Perform actions to simulate activity and prevent the system from sleeping
    print(">> No Mouse Movement Detected >> Pressing F24 Key and Move Mouse Cursor")
    # Simulate key presses
    pyautogui.press('numlock')
    time.sleep(0.5)
    pyautogui.press('numlock')
    time.sleep(5)
    pyautogui.press('f24')

    print(f'>> Num Lock key pressed at {datetime.now().time()}')
    # Move the mouse in a small pattern
    currentLocation = pyautogui.position()
    n_move = 5
    pyautogui.moveTo(currentLocation[0] + n_move, currentLocation[1] + n_move, duration=0.25)
    pyautogui.moveTo(currentLocation[0] - n_move, currentLocation[1] - n_move, duration=0.25)
    print(f'>> Mouse moved at {datetime.now().time()}')

try:
    # Main loop to check for mouse movement and perform stay-awake actions
    while True:
        print('>> Checking for mouse movement')
        currentLocation = pyautogui.position()
        if prevousLocation is None or prevousLocation == currentLocation:
            # If no mouse movement is detected, perform stay-awake actions
            stay_awake_actions()
        else:
            # If mouse movement is detected, update the previous location and do nothing
            print(f'>> Mouse Movement Detected >> Do Nothing')
        prevousLocation = currentLocation
        # Wait for 5 seconds before checking again
        time.sleep(5)
except Exception as exp:
    print(f'>><< Error: {exp}')
    print(errorMessage)
    sys.exit()
