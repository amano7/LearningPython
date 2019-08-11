import pyautogui as pa
import time

time.sleep(2)
pa.PAUSE = 0.2
pa.moveTo(200, 200)
distance = 700
inc = 35
pa.press('p')

pa.hotkey('command', '0')
pa.hotkey('command', '=')
pa.hotkey('command', '=')
pa.hotkey('command', '=')

while distance > 0:
    pa.click()
    pa.moveRel(distance, 0, duration=0.1)  # move right
    pa.click()
    distance-=inc
    pa.moveRel(0, distance, duration=0.1)   # move down
    pa.click()
    pa.moveRel(-distance, 0, duration=0.1)  # move left
    pa.click()
    distance-=inc
    pa.moveRel(0, -distance, duration=0.1)  # move up

pa.moveTo(150, 150, duration=0.5)
pa.press(['esc','v'])
pa.dragRel((distance + 200) * 2, (distance + 200) * 2, duration=0.5, button='left')   # move down

for i in range(5):
    try:
        pos = pa.locateCenterOnScreen('D.png', grayscale=True)
        break
    except Exception as ex:
        pa.press('d')
        pa.press('x')
pa.click()
pa.hotkey('command', '0')
pa.click()

