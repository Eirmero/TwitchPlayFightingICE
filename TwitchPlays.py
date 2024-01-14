import concurrent.futures
import random
import keyboard
import pydirectinput
import pyautogui
import TwitchPlays_Connection
from TwitchPlays_KeyCodes import *


TWITCH_CHANNEL = 'sucerry477' 

STREAMING_ON_TWITCH = True


YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID_HERE" 

YOUTUBE_STREAM_URL = None

#queue controller
MESSAGE_RATE = 0.5
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100 # Maximum number of threads you can process at a time 

last_time = time.time()
message_queue = []
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
active_tasks = []
pyautogui.FAILSAFE = False

# Count down before starting, so you have time to load up the game
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

if STREAMING_ON_TWITCH:
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(TWITCH_CHANNEL)
else:
    t = TwitchPlays_Connection.YouTube()
    t.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)

# arror_control
def hold_key(direction, duration=4):
    try:
        pyautogui.keyDown(direction)
        time.sleep(duration)
        pyautogui.keyUp(direction)
    except Exception as e:
        print(f"发生错误: {e}")

def handle_message(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print("Got this message from " + username + ": " + msg)

        #使用pyautogui来控制
        if msg == "left": 
            # pyautogui.keyDown('left')
            # pyautogui.keyUp('left')
            # time.sleep(0.1)
            # pyautogui.keyDown('left')
            # pyautogui.keyUp('left')
            # time.sleep(0.1)
            # pyautogui.keyDown('left')
            # pyautogui.keyUp('left')
            # time.sleep(0.1)
            # pyautogui.keyDown('left')
            # pyautogui.keyUp('left')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')

        if msg == "right": 
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "jump": 
            pyautogui.press('i')
            pyautogui.press('i')
            pyautogui.press('i')
            pyautogui.press('i')
            pyautogui.press('i')

        if msg == "crouch": 
            pyautogui.keyDown('k')
            time.sleep(4)
            pyautogui.keyUp('k')

        if msg == "a1": 
            pyautogui.press('t')
            pyautogui.press('t')
            pyautogui.press('t')
            pyautogui.press('t')
            pyautogui.press('t')

        if msg == "a2": 
            pyautogui.press('y')
            pyautogui.press('y')
            pyautogui.press('y')
            pyautogui.press('y')
            pyautogui.press('y')

        if msg == "attack":
            pyautogui.press('j')
            pyautogui.keyDown('j')
            time.sleep(0.5)
            pyautogui.press('t')
            pyautogui.keyUp('j')
            time.sleep(0.5)
            pyautogui.press('l')
            pyautogui.press('l')

        
        if msg == "pursue":
            pyautogui.keyDown('k')
            pyautogui.keyDown('l')
            pyautogui.keyUp('k')
            pyautogui.keyUp('l')
            time.sleep(0.05)
            pyautogui.press('t')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "avoid":
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
        
        if msg == "skill":
            pyautogui.keyDown('k')
            pyautogui.keyDown('j')
            pyautogui.keyUp('k')
            pyautogui.keyUp('j')
            time.sleep(0.05)
            pyautogui.press('t')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "super":
            pyautogui.keyDown('k')
            pyautogui.keyDown('j')
            pyautogui.keyUp('k')
            pyautogui.keyUp('j')
            time.sleep(0.05)
            pyautogui.press('u')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "r:attack":
            pyautogui.press('j')
            pyautogui.keyDown('j')
            time.sleep(0.5)
            pyautogui.press('t')
            pyautogui.keyUp('j')
            time.sleep(0.5)
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "r:pursue":
            pyautogui.keyDown('k')
            pyautogui.keyDown('l')
            pyautogui.keyUp('k')
            pyautogui.keyUp('l')
            time.sleep(0.05)
            pyautogui.press('t')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "r:avoid":
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "r:skill":
            pyautogui.keyDown('k')
            pyautogui.keyDown('j')
            pyautogui.keyUp('k')
            pyautogui.keyUp('j')
            time.sleep(0.05)
            pyautogui.press('t')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "r:super":
            pyautogui.keyDown('k')
            pyautogui.keyDown('j')
            pyautogui.keyUp('k')
            pyautogui.keyUp('j')
            time.sleep(0.05)
            pyautogui.press('u')
            pyautogui.press('l')
            pyautogui.press('l')

        if msg == "l:attack":
            pyautogui.press('j')
            pyautogui.keyDown('j')
            time.sleep(0.5)
            pyautogui.press('t')
            pyautogui.keyUp('j')
            time.sleep(0.5)
            pyautogui.press('l')
            pyautogui.press('l')
        
        if msg == "l:pursue":
            pyautogui.keyDown('k')
            pyautogui.keyDown('j')
            pyautogui.keyUp('k')
            pyautogui.keyUp('j')
            time.sleep(0.05)
            pyautogui.press('t')
            pyautogui.press('j')
            pyautogui.press('j')

        if msg == "l:avoid":
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')
            pyautogui.press('j')


        
        if msg == "l:skill":
            pyautogui.keyDown('k')
            pyautogui.keyDown('l')
            pyautogui.keyUp('k')
            pyautogui.keyUp('l')
            time.sleep(0.05)
            pyautogui.press('t')
            pyautogui.press('j')
            pyautogui.press('j')



        if msg == "l:super":
            pyautogui.keyDown('k')
            pyautogui.keyDown('l')
            pyautogui.keyUp('k')
            pyautogui.keyUp('l')
            time.sleep(0.05)
            pyautogui.press('u')
            pyautogui.press('j')
            pyautogui.press('j')

    except Exception as e:
        print("Encountered exception: " + str(e))


while True:

    active_tasks = [t for t in active_tasks if not t.done()]

    #Check for new messages
    new_messages = t.twitch_receive_messages();
    if new_messages:
        message_queue += new_messages; # New messages are added to the back of the queue
        message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

    messages_to_handle = []
    if not message_queue:
        # No messages in the queue
        last_time = time.time()
    else:
        # Determine how many messages we should handle now
        r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
        n = int(r * len(message_queue))
        if n > 0:
            # Pop the messages we want off the front of the queue
            messages_to_handle = message_queue[0:n]
            del message_queue[0:n]
            last_time = time.time();

    # If user presses Shift+Backspace, automatically end the program
    if keyboard.is_pressed('shift+backspace'):
        exit()

    if not messages_to_handle:
        continue
    else:
        for message in messages_to_handle:
            if len(active_tasks) <= MAX_WORKERS:
                active_tasks.append(thread_pool.submit(handle_message, message))
            else:
                print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')
 