import pyautogui
import time
import sys
pyautogui.PAUSE = 0.02
time.sleep(5)
for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                pyautogui.press('ENTER')
                print(str(i1)+str(i2)+str(i3)+str(i4))
                time.sleep(0.02)
                pyautogui.press(str(i1))
                pyautogui.press(str(i2))
                pyautogui.press(str(i3))
                pyautogui.press(str(i4))
                pyautogui.press('ENTER')
                while True:
                    try:
                        pyautogui.locateOnScreen('PINKOD2.png', grayscale=True)
                        print(str(i1)+str(i2)+str(i3)+str(i4))
                        exit()
                    except:
                        try:
                            pyautogui.locateOnScreen('PINKOD.png', grayscale=True)
                            pyautogui.press('ESC')
                            break
                        except:
                            try:
                                pyautogui.locateOnScreen('PINKOD3.png', grayscale=True)
                                pyautogui.press(str(i1))
                                pyautogui.press(str(i2))
                                pyautogui.press(str(i3))
                                pyautogui.press(str(i4))
                                pyautogui.press('ENTER')
                            except:
                                pass
