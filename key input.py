from pynput.keyboard import Listener

print("start")
    
def on_press(key):
    print("Key pressed: {0}".format(key))

def on_release(key):
    print("Key released: {0}".format(key))

    
with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
    listener.join()
    