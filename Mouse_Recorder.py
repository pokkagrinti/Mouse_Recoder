from win32api import *
from time import sleep
import keyboard  
import win32api, win32con

    

def recorder():
    with open("recording.txt", "w") as f:
        while True:
            sleep(0.01)
            x, y = GetCursorPos()
            print("{},{}".format(x, y))
            f.write("{},{}\n".format(x, y))
            try:  
                if keyboard.is_pressed('q'):  
                    print('Stopped Recording!')
                    break  
            except:
                break


def playback():
    mouse_list = []
    with open("recording.txt", "r") as f:
        for i in f:
            i = i.strip('\n')
            i = i.split(",")
            for j in range(0, len(i)): 
                i[j] = int(i[j])
            mouse_list.append(i)

    for i in mouse_list:
        if keyboard.is_pressed('q'):  
                print('Stopped Playing')
                break
        sleep(0.02)
        x, y = i
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/1920*65535.0), int(y/1080*65535.0))

def main():
    
    while True:
        try:  
            if keyboard.is_pressed('f1'):  
                print('Recording...')
                recorder()
            if keyboard.is_pressed('f2'):  
                print('Playback...')
                playback()
                print('Playback Finished!...')
                
            if keyboard.is_pressed('f3'):
                break
            
        except:
             break

if __name__ == "__main__":
    main()
