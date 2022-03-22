from pynput import mouse, keyboard
import pyautogui

#pyautogui.PAUSE = 0.01
mouse_listening = False
#position_press = (-1,-1)
#position_release = (-1,-1)

position_click = [[-1,-1], [-1,-1]]

def on_click(x, y, button, pressed):
    global mouse_listening, position_click
    #print('>==={} at {}'.format('Pressed' if pressed else 'Release', (x,y)))
    if pressed:
        if position_click[0][0] < 0:
            position_click[0] = [x,y]
            print(">=== Please R-click mouse for button-right of OCR zone")
        else:
            position_click[1] = [x,y]
            mouse_listening = True

def listener_mouse():
    global mouse_listening
    print(">=== Please R-click mouse for top-left of OCR zone")
    while not mouse_listening:
        pass

def start_listen():
    global position_click
    mouse_listener = mouse.Listener(on_click = on_click)
    mouse_listener.start()
    listener_mouse()
    mouse_listener.stop()
    
    x_left = position_click[0][0]
    x_right = position_click[1][0]
    y_top = position_click[0][1]
    y_button = position_click[1][1]
    if position_click[0][0] > position_click[1][0]:
        x_left = position_click[1][0]
        x_right = position_click[0][0]
    if position_click[0][1] > position_click[1][1]:
        y_top = position_click[1][1]
        y_button = position_click[0][1]

    return (x_left, y_top, x_right, y_button)
    
#start_listen()
