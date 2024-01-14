from pynput.keyboard import Listener, Key
import time

# 全局变量来存储上一次按键的时间
last_time_pressed = time.time()

def on_press(key):
    global last_time_pressed
    current_time = time.time()
    delay = current_time - last_time_pressed
    last_time_pressed = current_time

    try:
        print(f"按键: {key.char}, 延迟: {delay} 秒")
    except AttributeError:
        print(f"按键: {key}, 延迟: {delay} 秒")

# 监听键盘事件
with Listener(on_press=on_press) as listener:
    listener.join()




